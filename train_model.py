"""
Phase 2: Predictive Modeling Engine
Domain: Premium Health Insurance & Wellness Retention Analytics
Author: Dereck Ceballos
"""

import numpy as np
import pandas as pd
import awswrangler as wr
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

print("[INFO] Fetching clean data from AWS Glue Catalog...")
df = wr.athena.read_sql_query(
    sql='SELECT * FROM "wellness_services_db"."wellness_analytics_data_drceballos3278"',
    database="wellness_services_db"
)

# Find the target column dynamically
if 'churn_numeric' in df.columns:
    y = df['churn_numeric']
elif 'churn' in df.columns:
    y = df['churn']
elif 'cancellation/attrition' in df.columns:
    y = np.where(df['cancellation/attrition'] == 'Yes', 1, 0)
else:
    potential_churn_cols = [c for c in df.columns if 'cancel' in c or 'attrit' in c or 'churn' in c]
    if potential_churn_cols:
        y = np.where(df[potential_churn_cols] == 'Yes', 1, 0)
    else:
        raise KeyError("Could not find the target Churn/Cancellation column.")

# Drop metadata columns to isolate predictive features
cols_to_drop = ['member_id', 'customer_id', 'cancellation/attrition', 'churn_status', 'churn_numeric', 'churn']
X = df.drop(columns=[c for c in cols_to_drop if c in df.columns], errors='ignore')

# Handle categorical encoding
X_encoded = pd.get_dummies(X, drop_first=True)

# Train/Test Split (Stratified to handle class balance)
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42, stratify=y)

# Model Training
print("\n[INFO] Training the Predictive Model (Random Forest)...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\n[SUCCESS] Model Predictive Accuracy: {accuracy * 100:.2f}%")

# Inject Predictions & Export for Power BI
print("\n[INFO] Injecting predictions and exporting full dataset...")
df['Churn_Prediction'] = model.predict(X_encoded)
df.to_csv("Wellness_customer_churn_with_predictions.csv", index=False)
print("[SUCCESS] Deployment File Generated Successfully.")
