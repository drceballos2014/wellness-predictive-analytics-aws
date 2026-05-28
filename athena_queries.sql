-- Phase 1: Exploratory Data Analysis (EDA) via Amazon Athena
-- Purpose: Quantify the financial leak and identify critical attrition zones.

-- 1. Global Retention Health & Attrition Rate
SELECT 
    COUNT(*) as total_active_members,
    SUM(CASE WHEN "cancellation/attrition" = 'Yes' THEN 1 ELSE 0 END) as total_cancellations,
    ROUND((SUM(CASE WHEN "cancellation/attrition" = 'Yes' THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2) as global_churn_rate
FROM "wellness_services_db"."wellness_analytics_data_drceballos3278";


-- 2. Financial Leak Analysis by Membership Tier (Premium Crisis Detection)
SELECT 
    membership_tier,
    COUNT(*) as total_subscribers,
    SUM(CASE WHEN "cancellation/attrition" = 'Yes' THEN 1 ELSE 0 END) as cancellations,
    ROUND((SUM(CASE WHEN "cancellation/attrition" = 'Yes' THEN 1 ELSE 0 END) * 100.0) / COUNT(*), 2) as tier_churn_rate,
    ROUND(SUM(CASE WHEN "cancellation/attrition" = 'Yes' THEN monthly_premium ELSE 0 END), 2) as monthly_revenue_loss,
    ROUND(SUM(CASE WHEN "cancellation/attrition" = 'Yes' THEN monthly_premium ELSE 0 END) * 12, 2) as annualized_revenue_loss
FROM "wellness_services_db"."wellness_analytics_data_drceballos3278"
GROUP BY membership_tier
ORDER BY annualized_revenue_loss DESC;


-- 3. Operational Fuga Analysis: Telehealth Access Impact within Comprehensive Health
SELECT 
    telehealth_access,
    COUNT(*) as comprehensive_subscribers,
    SUM(CASE WHEN "cancellation/attrition" = 'Yes' THEN 1 ELSE 0 END) as cancellations,
    ROUND(SUM(CASE WHEN "cancellation/attrition" = 'Yes' THEN monthly_premium ELSE 0 END) * 12, 2) as at_risk_arr
FROM "wellness_services_db"."wellness_analytics_data_drceballos3278"
WHERE membership_tier = 'Comprehensive Health'
GROUP BY telehealth_access;
