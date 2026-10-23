# 🛡️ Financial Fraud Detection & IT Access Controls Audit

> **Automated IT Controls Audit Simulation & SQL Anomaly Detection Pipeline** validating Segregation of Duties (SoD), user privilege escalation, and off-hours transactional spikes across 50,000+ logs adhering to the **CIA Triad** (Confidentiality, Integrity, Availability) and **SOX compliance**.

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![SQL](https://img.shields.io/badge/SQL-Advanced%20Audit-orange?style=flat-square)](#)
[![Compliance](https://img.shields.io/badge/Compliance-SOX%20%2F%20ITGC-red?style=flat-square)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

---

## 📌 Executive Summary

Internal financial fraud and access privilege abuse represent catastrophic organizational risks. Inadequate Segregation of Duties (SoD) enables unauthorized transactions and compromised ledger records.

This project implements:
1. **Automated Audit Pipeline**: Scans transaction and system logs to detect anomalous operator behavior.
2. **Segregation of Duties (SoD) Matrix**: Enforces dual-authorization constraints (e.g., junior billing personnel cannot authorize disbursements or modify payroll tables).
3. **Temporal Anomaly Flagging**: Highlights off-hours system activity (11:00 PM – 5:00 AM) to uncover stealth data tampering.
4. **Adherence to CIA Triad**: Ensures confidentiality of sensitive payroll data, integrity of financial entries, and availability of immutable audit trails.

---

## 📂 Repository Structure

```plaintext
financial-fraud-it-audit-controls/
│
├── audit_simulation.py        # Generates logs & executes Python compliance tests
├── audit_rules.sql            # Production SQL queries for auditor review
├── data/
│   ├── financial_audit_logs.csv       # Scanned log records
│   └── audit_summary_report.json      # Structured auditor executive report
└── README.md                  # Project documentation & audit methodology
```

---

## 🚀 Quick Execution

```bash
# Run the audit engine and generate JSON report
python audit_simulation.py
```

---

## 👤 Author
**Bachu Uttej Siva Sai Kumar Reddy**
- **GitHub**: [@uttej2](https://github.com/uttej2)
- **Portfolio**: [https://uttej2.github.io](https://uttej2.github.io)
- **LinkedIn**: [Connect on LinkedIn](https://linkedin.com/in/uttej-sai)
