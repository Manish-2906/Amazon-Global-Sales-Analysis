# 📊 Amazon Global Superstore Sales Analysis

This project presents a complete end-to-end data analysis pipeline on Amazon's Global Superstore dataset (2012–2016). It covers data ingestion, exploration, transformation, and interactive dashboard creation to uncover business insights.

---

## 🚀 Project Objectives

- Ingest raw Excel data into a structured MySQL database
- Perform exploratory data analysis and feature engineering using Python
- Analyze key metrics like profit, sales, delivery time, and discounts
- Identify loss-making products, profitable customers, and market trends
- Build a Power BI dashboard for interactive decision-making

---

## 🧰 Tools & Technologies

| Tool           | Purpose                          |
|----------------|----------------------------------|
| Python         | Data ingestion, transformation   |
| MySQL          | Database storage and querying    |
| Pandas, Seaborn| EDA & visualization              |
| Power BI       | Dashboard creation               |
| JupyterLab     | Notebook-based analysis          |
| SQLAlchemy     | Python ↔ MySQL integration       |
| Logging Module | Pipeline monitoring              |

---

## 🧱 Project Structure

![Untitled Diagram drawio](https://github.com/user-attachments/assets/839bb15b-b850-455d-ada7-631a662d798e)


## 🔄 End-to-End Workflow

1. **Ingestion**  
   Load multiple `.xlsx` files into MySQL using `pandas.to_sql()` in Python.

2. **Logging**  
   Logged ingestion status, error handling, and processing time.

3. **EDA (Jupyter)**  
   - Outlier detection (IQR method)
   - Correlation heatmaps
   - Feature engineering: `ord_to_deli`, `year`, `profit_margin`

4. **Dashboard (Power BI)**  
   - Key Metrics: Total Sales, Quantity, AOV, Delivery Days
   - Filters: Year, Segment, Market
   - Charts: Top Profitable Products, Loss-Making Categories, Market-wise Sales

---

## 📈 Key Business Insights

- High discounts negatively impact profit (Corr: -0.85)
- Tables & Bookcases are top loss-making sub-categories
- US, Turkey, Nigeria show heavy profit losses
- Asia-Pacific and Consumer segments dominate sales
- Some customers like **Tamara Chand** and **Raymond Buch** drive high profit

---

## 📸 Dashboard Preview

![Amazon Dashboard](https://github.com/user-attachments/assets/5a5bde83-dfc3-44eb-894e-41eb49437206)


---

## 🧠 Recommendations

- Optimize high-loss products with pricing & shipping review
- Implement loyalty programs for high-value customers
- Reduce unnecessary deep discounts to improve margins
- Use sales trends for inventory planning and budgeting

---

## 📎 Files

- `Ingestion_db.py` → Loads Excel to MySQL with logging
- `Amazon_EDA.ipynb` → Full exploratory analysis in Jupyter
- `Amazon_Dashboard.pbix` → Interactive Power BI file
- `Amazon_Dashboard.png` → Dashboard visual
- `Amazon_EDA_Report.pdf` → PDF version of EDA for offline review

---

## 👨‍💻 Author

**Manish Divekar**  
*Aspiring Data Analyst | Python • SQL • Power BI*  
📫 [LinkedIn] www.linkedin.com/in/manish-analyst

---
