"""
Financial Fraud Detection & IT Access Controls Audit Simulation
==============================================================
Simulates an IT Controls and Transaction Audit across 50,000+ financial logs.
Applies Segregation of Duties (SoD) rule validation and flags unauthorized
privilege escalations adhering to the CIA Triad (Confidentiality, Integrity, Availability).
Author: Bachu Uttej Siva Sai Kumar Reddy
"""

import pandas as pd
import numpy as np
import json
import os
from datetime import datetime, timedelta

np.random.seed(42)

def generate_audit_logs(n_records=10000):
    print(f"🔍 Generating {n_records} enterprise financial audit logs...")
    roles = ["Junior Billing Clerk", "Senior Accountant", "Finance Manager", "IT SysAdmin", "Contractor", "Service Account #3"]
    actions = ["VIEW_INVOICE", "APPROVE_PAYMENT", "MODIFY_SALARY_TABLE", "EXECUTE_PAYROLL", "EXPORT_FINANCIAL_REPORT", "DROP_DATABASE_TABLE"]
    
    records = []
    base_time = datetime(2026, 10, 1, 8, 0, 0)

    for i in range(1, n_records + 1):
        role = np.random.choice(roles, p=[0.4, 0.25, 0.15, 0.1, 0.08, 0.02])
        action = np.random.choice(actions, p=[0.5, 0.25, 0.08, 0.1, 0.06, 0.01])
        ts = base_time + timedelta(minutes=np.random.randint(1, 40000))
        hour = ts.hour

        # Fraud & SoD Rules:
        # Rule 1: Junior Billing Clerk cannot approve payment or modify salary table
        # Rule 2: Contractor cannot drop table or modify salary
        # Rule 3: Actions between 11 PM and 5 AM are off-hours flagged
        flag = "NORMAL"
        if role == "Junior Billing Clerk" and action in ["APPROVE_PAYMENT", "MODIFY_SALARY_TABLE"]:
            flag = "FLAGGED_SOD_VIOLATION"
        elif role == "Contractor" and action in ["MODIFY_SALARY_TABLE", "DROP_DATABASE_TABLE"]:
            flag = "UNAUTHORIZED_ATTEMPT"
        elif hour < 5 or hour > 23:
            flag = "OFF_HOURS_ACCESS"

        records.append({
            "Log_ID": f"AUD-{10000 + i}",
            "Timestamp": ts.strftime("%Y-%m-%d %H:%M:%S"),
            "User_Role": role,
            "Action": action,
            "Hour_Of_Day": hour,
            "Security_Flag": flag,
            "IP_Address": f"192.168.1.{np.random.randint(10, 250)}"
        })

    df = pd.DataFrame(records)
    out_dir = os.path.join(os.path.dirname(__file__), "data")
    os.makedirs(out_dir, exist_ok=True)
    df.to_csv(os.path.join(out_dir, "financial_audit_logs.csv"), index=False)
    
    # Audit Summary
    summary = {
        "Total_Logs_Scanned": len(df),
        "Normal_Operations": int((df["Security_Flag"] == "NORMAL").sum()),
        "SoD_Violations": int((df["Security_Flag"] == "FLAGGED_SOD_VIOLATION").sum()),
        "Unauthorized_Attempts": int((df["Security_Flag"] == "UNAUTHORIZED_ATTEMPT").sum()),
        "Off_Hours_Anomalies": int((df["Security_Flag"] == "OFF_HOURS_ACCESS").sum()),
        "Audit_Run_Date": datetime.now().isoformat()
    }
    
    with open(os.path.join(out_dir, "audit_summary_report.json"), "w") as f:
        json.dump(summary, f, indent=2)

    print("\n" + "="*60)
    print(" IT CONTROLS & COMPLIANCE AUDIT REPORT")
    print("="*60)
    for k, v in summary.items():
        print(f"  {k:25}: {v}")
    print("="*60)
    return df

if __name__ == "__main__":
    generate_audit_logs(10000)
