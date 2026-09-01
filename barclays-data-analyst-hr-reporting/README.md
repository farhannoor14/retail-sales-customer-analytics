# HR Reporting & Risk Analytics

## Portfolio Project — Data Analyst

A portfolio project designed around common Data Analyst responsibilities in banking and enterprise environments: HR reporting, data quality, risk and controls, KPI reporting, stakeholder dashboards, and actionable recommendations.

> **Note:** This is an independent portfolio project using synthetic data. It is not affiliated with or based on confidential Barclays data.

## Business Objective

Build a reliable reporting workflow that transforms employee, attendance, performance, and compliance data into actionable insights for operational and management decision-making.

## Tools

- Python (Pandas) — data cleaning, validation, exploratory analysis
- SQL — KPI extraction, joins, aggregations, exception analysis
- Power BI — interactive reporting and dashboard design
- Excel — reconciliation, validation and reporting support

## Key Questions

1. What is the current headcount by department and location?
2. Which departments have the highest attrition risk?
3. How do attendance and performance vary across teams?
4. Are there data-quality exceptions or missing records that could affect reporting?
5. Which compliance/control indicators require attention?
6. What trends should management monitor for operational improvement?

## Data Workflow

`Raw Sources → Data Quality Checks → Cleaning → SQL Analysis → KPI Dataset → Power BI Dashboard → Business Recommendations`

## Controls & Data Quality

The project includes checks for missing values, duplicate employee IDs, invalid dates, inconsistent department values, attendance anomalies, and compliance exceptions. Exceptions are documented for review rather than silently removed.

## Dashboard Pages

### 1. Executive Overview
- Headcount
- Attrition rate
- Average performance score
- Attendance rate
- Compliance exception count

### 2. Workforce Analysis
- Headcount by department/location
- Joiners vs leavers
- Tenure distribution
- Attrition trend

### 3. Risk & Controls
- Compliance exceptions
- Attendance anomalies
- Missing/invalid records
- High-risk departments
- Exception status and ageing

### 4. Performance & Insights
- Performance by department
- Training completion
- Absence patterns
- Recommendations for operational improvement

## Outcome

The project demonstrates an end-to-end analytical approach covering data manipulation, data quality, reporting, risk awareness, stakeholder communication, and continuous improvement.

## Files

- `data/hr_analytics_synthetic.csv` — synthetic employee reporting dataset
- `sql/hr_reporting_analysis.sql` — reporting and control queries
- `src/hr_analysis.py` — Python cleaning and analysis workflow
- `src/data_quality_checks.py` — validation and exception checks
