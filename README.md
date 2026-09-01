# Retail Sales & Customer Analytics

End-to-end Data Analyst portfolio project focused on turning transactional retail data into actionable business insights.

## Business Questions
- Which categories and cities drive the most revenue?
- Which products contribute most to profit?
- How do discounts affect sales and profitability?
- Which customers are high-value and how concentrated is revenue?
- What trends and operational issues should management act on?

## Tools
**Python, Pandas, NumPy, SQL, Excel, Power BI, Tableau, Data Visualization, Exploratory Data Analysis (EDA)**

## Workflow
1. Data collection and validation
2. Data cleaning and quality checks
3. Exploratory data analysis
4. KPI and customer segmentation analysis
5. SQL-based business queries
6. Dashboard-ready datasets and visual reporting
7. Business recommendations

## Dataset
The included dataset is **synthetic portfolio data** created for demonstration and interview purposes. It contains 40 orders across six Indian cities and five product categories.

## Sample KPIs
| KPI | Value |
|---|---:|
| Total Sales | ₹536,801.75 |
| Total Profit | ₹151,415.19 |
| Orders | 40 |
| Unique Customers | 18 |
| Units Sold | 125 |

## Key Observations
- Electronics is the highest-revenue category in the sample.
- Mumbai and Delhi are the strongest cities by sales.
- Discounting should be monitored alongside profit rather than revenue alone.
- Customer-level aggregation enables identification of repeat and high-value customers.

## Repository Structure
```text
retail-sales-customer-analytics/
├── data/
│   └── retail_sales.csv
├── sql/
│   └── business_queries.sql
├── src/
│   ├── analysis.py
│   └── data_quality_checks.py
├── requirements.txt
└── README.md
```

## How to Run
```bash
pip install -r requirements.txt
python src/analysis.py
python src/data_quality_checks.py
```

## Dashboard Ideas
Build a Power BI/Tableau dashboard with:
- KPI cards: Sales, Profit, Orders, Customers
- Monthly sales and profit trend
- Sales by category and city
- Top products by revenue/profit
- Discount vs. profit analysis
- Customer contribution and repeat-order view

## Skills Demonstrated
Data cleaning, validation, KPI development, SQL, Python analysis, aggregation, customer analytics, data visualization, business storytelling, reporting, attention to detail, and data-driven recommendations.
