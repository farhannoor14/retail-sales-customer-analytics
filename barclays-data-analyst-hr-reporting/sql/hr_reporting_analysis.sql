-- HR Reporting & Analytics: SQL Analysis

-- 1. Headcount by department
SELECT Department, COUNT(*) AS Headcount
FROM hr_analytics_synthetic
WHERE Status = 'Active'
GROUP BY Department
ORDER BY Headcount DESC;

-- 2. Average attendance and performance by department
SELECT Department,
       ROUND(AVG(Attendance_Rate), 2) AS Avg_Attendance_Rate,
       ROUND(AVG(Performance_Score), 2) AS Avg_Performance
FROM hr_analytics_synthetic
WHERE Status = 'Active'
GROUP BY Department
ORDER BY Avg_Attendance_Rate ASC;

-- 3. Compliance exceptions requiring review
SELECT Employee_ID, Department, Location, Compliance_Exceptions
FROM hr_analytics_synthetic
WHERE Compliance_Exceptions > 0
ORDER BY Compliance_Exceptions DESC;

-- 4. Employees with potential attendance risk
SELECT Employee_ID, Department, Attendance_Rate, Monthly_Absence_Days
FROM hr_analytics_synthetic
WHERE Attendance_Rate < 90
   OR Monthly_Absence_Days >= 4
ORDER BY Attendance_Rate ASC;

-- 5. Training completion below target
SELECT Department,
       COUNT(*) AS Employees_Below_Target
FROM hr_analytics_synthetic
WHERE Training_Completion < 90
GROUP BY Department
ORDER BY Employees_Below_Target DESC;

-- 6. Overall KPI summary
SELECT COUNT(*) AS Total_Employees,
       SUM(CASE WHEN Status = 'Active' THEN 1 ELSE 0 END) AS Active_Employees,
       SUM(CASE WHEN Status = 'Leaver' THEN 1 ELSE 0 END) AS Leavers,
       ROUND(AVG(Attendance_Rate), 2) AS Avg_Attendance,
       ROUND(AVG(Performance_Score), 2) AS Avg_Performance,
       SUM(Compliance_Exceptions) AS Total_Compliance_Exceptions
FROM hr_analytics_synthetic;

-- 7. High-priority control exceptions
SELECT Employee_ID, Department, Compliance_Exceptions, Training_Completion, Attendance_Rate
FROM hr_analytics_synthetic
WHERE Compliance_Exceptions >= 2
   OR (Training_Completion < 80 AND Attendance_Rate < 90)
ORDER BY Compliance_Exceptions DESC, Attendance_Rate ASC;
