import pandas as pd

FILE = "data/hr_analytics_synthetic.csv"
REQUIRED = ["Employee_ID", "Department", "Location", "Join_Date", "Status",
            "Performance_Score", "Attendance_Rate", "Training_Completion",
            "Compliance_Exceptions", "Monthly_Absence_Days", "Salary_Band"]

df = pd.read_csv(FILE)

checks = {
    "row_count": len(df),
    "duplicate_employee_ids": int(df["Employee_ID"].duplicated().sum()),
    "missing_values": int(df.isna().sum().sum()),
    "invalid_attendance": int((~df["Attendance_Rate"].between(0, 100)).sum()),
    "invalid_training": int((~df["Training_Completion"].between(0, 100)).sum()),
    "negative_absence_days": int((df["Monthly_Absence_Days"] < 0).sum()),
    "negative_compliance_exceptions": int((df["Compliance_Exceptions"] < 0).sum()),
}

print("=== DATA QUALITY / CONTROL CHECKS ===")
for name, result in checks.items():
    print(f"{name}: {result}")

print("\n=== EXCEPTIONS ===")
exceptions = df[(df["Compliance_Exceptions"] > 0) |
                (df["Attendance_Rate"] < 90) |
                (df["Training_Completion"] < 90)]
print(exceptions[["Employee_ID", "Department", "Location", "Attendance_Rate",
                  "Training_Completion", "Compliance_Exceptions"]].to_string(index=False))
