-- ============================================================================
-- IT CONTROLS & TRANSACTION FRAUD DETECTION AUDIT RULES (SQL)
-- Compliance: CIA Triad, SOX Section 404, Segregation of Duties (SoD)
-- Author: Bachu Uttej Siva Sai Kumar Reddy
-- ============================================================================

-- Rule 1: Segregation of Duties (SoD) Violation Detection
-- Identifies junior clerks attempting payment approvals or payroll alterations
SELECT 
    log_id,
    timestamp,
    user_role,
    action,
    ip_address
FROM financial_audit_logs
WHERE user_role = 'Junior Billing Clerk'
  AND action IN ('APPROVE_PAYMENT', 'MODIFY_SALARY_TABLE')
ORDER BY timestamp DESC;

-- Rule 2: High-Risk Off-Hours Anomalies (Between 11:00 PM and 5:00 AM)
SELECT 
    log_id,
    timestamp,
    user_role,
    action,
    hour_of_day,
    ip_address
FROM financial_audit_logs
WHERE hour_of_day < 5 OR hour_of_day > 23
ORDER BY timestamp DESC;

-- Rule 3: Third-Party Contractor Access Control Boundary Checks
SELECT 
    log_id,
    timestamp,
    user_role,
    action,
    ip_address
FROM financial_audit_logs
WHERE user_role = 'Contractor'
  AND action IN ('MODIFY_SALARY_TABLE', 'DROP_DATABASE_TABLE');

-- Rule 4: Audit Event Rollup by User Role & Security Flag
SELECT 
    user_role,
    security_flag,
    COUNT(*) AS incident_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY user_role), 2) AS incident_pct_within_role
FROM financial_audit_logs
GROUP BY user_role, security_flag
ORDER BY user_role, incident_count DESC;
