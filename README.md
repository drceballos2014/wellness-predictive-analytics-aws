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
