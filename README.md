# Customer Retention & Predictive Analytics in Health & Wellness Services

## Business Problem
Customer retention is a critical growth driver for health insurance and wellness subscription models. Retaining an existing member is significantly more cost-effective than acquiring a new one. This project builds an end-to-end cloud data pipeline and predictive machine learning model to identify members at risk of canceling their subscriptions, enabling marketing teams to deploy proactive retention strategies.

## Data Source & Recontextualization
This project utilizes the industry-standard IBM Customer Churn dataset. To better align with commercial services and health industries, columns have been recontextualized to represent a premium wellness/health membership program:


| Original Column (IBM) | Project Column Name | Business Meaning |
| :--- | :--- | :--- |
| **customerID** | Patient_ID / Member_ID | Unique identifier for each health plan subscriber. |
| **tenure** | Account_Age_Months | Total months the subscriber has been active. |
| **Contract** | Plan_Type | Subscription billing cycle (Month-to-month, 1-Year, 2-Year). |
| **MonthlyCharges** | Monthly_Premium | Monthly cost of the insurance or wellness plan. |
| **InternetService** | Membership_Tier | Access levels: Basic Care, Standard Wellness, or Premium Care. |
| **PhoneService** | Telehealth_Access | Subscription includes 24/7 virtual doctor consultations. |
| **MultipleLines** | Family_AddOns | Additional coverage extensions for family members. |
| **OnlineSecurity** | Critical_Illness_Insurance | Complementary coverage for major medical accidents. |
| **OnlineBackup** | Digital_Health_Record | Secure cloud access to personal medical histories. |
| **DeviceProtection** | Medical_Equipment_Coverage | Home monitoring device assistance or 24/7 ambulance. |
| **TechSupport** | Care_Concierge_Service | Priority specialist scheduling and reimbursement support. |
| **StreamingTV** | OnDemand_Fitness_App | Premium access to integrated fitness/workout apps. |
| **StreamingMovies** | Nutrition_MentalHealth_App| Premium access to mental health and meal-planning apps. |
| **Churn** | Cancellation / Attrition | Goal variable: Has the user canceled the plan? (Yes/No). |

## Cloud Architecture (AWS Serverless)
*   **Storage:** Raw dataset hosted on **Amazon S3**.
*   **ETL & Transformation:** Automated data cleaning and type validation using **AWS Glue**.
*   **Data Exploration:** SQL queries via **Amazon Athena** to uncover initial business trends.
*   **Predictive AI:** Automated machine learning model trained using **Amazon SageMaker**.
*   **Data Warehouse:** Structured insights stored in **Amazon Redshift**.
*   **Visualization:** Interactive executive dashboard built on **Power BI / QuickSight**.

*   ## Exploratory Data Analysis (EDA) & Business Insights (SQL via Athena)

Before training the AI models, a comprehensive business analysis was performed using **Amazon Athena** to diagnose the company's retention health. The initial results revealed critical financial leaks:

### 1. Global Retention Health
*   **Total Active Members Analyzed:** 7,080
*   **Total Historical Cancellations:** 1,869
*   **Global Attrition (Churn) Rate:** **26.40%**
*   *Business Impact:* A churn rate higher than 20% is a critical red flag for health and wellness subscription models, indicating that more than a quarter of the portfolio is leaking out.

### 2. High-Value Attrition Crisis (Membership Tier Analysis)
By executing granular SQL queries to segment users by tier, a major revenue leak was discovered within the premium segment:

*   **Premium Wellness Plan (High-Tier):** This segment holds the highest churn concentration with a staggering **41.89% Churn Rate** (1,297 cancellations out of 3,096 subscribers). 
*   **Financial Leak:** This premium leakage represents a direct loss of **$114,300.05 USD per month** ($1.37M USD annualized).
*   **Basic Care Plan (Low-Tier):** Shows strong stability with only a **7.40% Churn Rate** (113 cancellations).
*   *Strategic Conclusion:* The attrition issue is product-specific, concentrated in the premium high-cost tier. This justifies deploying an Automated Machine Learning (ML) solution to score each premium user's probability of leaving before they cancel.

## Machine Learning & Predictive Modeling (Python via SageMaker JupyterLab)

An advanced Predictive Analytics solution was deployed within a secure, administrative **Amazon SageMaker** workspace to anticipate customer attrition. A **Random Forest Classifier** was trained directly in a JupyterLab environment, pulling structured features from the AWS Glue Data Catalog.

### Executive Model Performance & Business Metrics

*   **Global Predictive Accuracy:** **77.29%**
*   **Active Customer Retention (Class 0 - Stay):** 82% Precision / 88% Recall
*   **At-Risk Customer Detection (Class 1 - Churn):** 59% Precision / 47% Recall
*   **Dataset Support Evaluation:** 1,409 unseen evaluation records.

### Commercial ROI Valuation
By successfully anticipating **47% of customer cancellations** within the high-value segments, the business can deploy proactive marketing strategies (e.g., personalized health discounts, concierge check-ins) to mitigate the premium attrition crisis. This predictive capability translates to an estimated **monthly savings of $53,700 USD**, preserving over **$644,000 USD in annualized recurring revenue (ARR)** for the Health & Wellness organization.
