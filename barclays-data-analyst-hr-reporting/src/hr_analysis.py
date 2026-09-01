import pandas as pd

PATH = "data/hr_analytics_synthetic.csv"
df = pd.read_csv(PATH, parse_dates=["Join_Date"])

# Standardise text fields
for col in ["Department", "Location", "Status", "Salary_Band"]:
    df[col] = df[col].astype(str).str.strip()

# Derived metrics
reference_date = pd.Timestamp("2025-01-01")
df["Tenure_Years"] = (reference_date - df["Join_Date"]).dt.days / 365.25
df["Attendance_Risk"] = df["Attendance_Rate"] < 90
df["Control_Risk"] = (df["Compliance_Exceptions"] > 0) | (df["Training_Completion"] < 90)

active = df[df["Status"] == "Active"]

print("=== EXECUTIVE KPIs ===")
print("Total employees:", len(df))
print("Active employees:", len(active))
print("Leavers:", (df["Status"] == "Leaver").sum())
print("Attrition rate:", f"{(df['Status'].eq('Leaver').mean()):.1%}")
print("Average attendance:", f"{df['Attendance_Rate'].mean():.1f}%")
print("Average performance:", f"{df['Performance_Score'].mean():.2f}/5")
print("Compliance exceptions:", int(df["Compliance_Exceptions"].sum()))

print("\n=== DEPARTMENT SCORECARD ===")
scorecard = (active.groupby("Department", as_index=False)
             .agg(Headcount=("Employee_ID", "count"),
                  Avg_Attendance=("Attendance_Rate", "mean"),
                  Avg_Performance=("Performance_Score", "mean"),
                  Control_Exceptions=("Compliance_Exceptions", "sum"),
                  Avg_Training=("Training_Completion", "mean"))
             .sort_values("Control_Exceptions", ascending=False))
print(scorecard.to_string(index=False))

print("\n=== DATA QUALITY ===")
print("Duplicate employee IDs:", int(df["Employee_ID"].duplicated().sum()))
print("Missing values:", int(df.isna().sum().sum()))
print("Invalid attendance values:", int((~df["Attendance_Rate"].between(0, 100)).sum()))
print("Invalid training values:", int((~df["Training_Completion"].between(0, 100)).sum()))

print("\n=== HIGH PRIORITY EXCEPTIONS ===")
exceptions = df[(df["Compliance_Exceptions"] >= 2) |
                ((df["Training_Completion"] < 80) & (df["Attendance_Rate"] < 90))]
print(exceptions[["Employee_ID", "Department", "Attendance_Rate", "Training_Completion", "Compliance_Exceptions"]]
      .sort_values("Compliance_Exceptions", ascending=False).to_string(index=False))
