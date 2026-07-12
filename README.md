# Task-1 :- Netflix Movies and TV Shows – Data Cleaning & Preprocessing

## 📌 Project Overview
This project focuses on the initial phase of the data analysis pipeline: **Data Cleaning and Preprocessing**. Using a raw dataset of Netflix movies and TV shows, the objective was to identify potential inconsistencies, handle formatting discrepancies, and ensure data integrity to prepare the dataset for seamless future analysis or machine learning modeling.

This task is completed as part of the **Data Analyst Internship** at **Alabs** under the **Ministry of MSME, Govt. of India**.

---

## 🛠️ Tools & Technologies Used
* **Language:** Python
* **Libraries:** Pandas (for data manipulation and preprocessing)
* **Dataset Source:** Kaggle (Netflix Movies and TV Shows)

---

## 🧼 Data Cleaning Pipeline & Transformation Summary
A structured preprocessing workflow was executed to clean the raw dataset. Below is the summary of the operations performed:

* **Header Standardization:** All column headers were transformed into lowercase `snake_case` to ensure uniformity and prevent syntax issues during queries.
* **Text Normalization:** Standardized categorical text fields by trimming accidental trailing/leading whitespaces and normalizing character casing for consistency (e.g., in the `rating` column).
* **Date-Time Alignment:** Converted the `date_added` column from an inconsistent text format into a proper `datetime` object, exporting the final values in the standardized `YYYY-MM-DD` format.
* **Data Integrity & Quality Check:** 
  * Audited the dataset for missing values; no null fields were present in the critical working columns.
  * Checked for duplicate records; verified that the source file contained zero duplicate rows, ensuring no data removal or imputation was required.
* **Data Type Validation:** Enforced correct data schema constraints, explicitly verifying that `release_year` is stored as a numeric integer type.

---


# Task 2 :- 📊 Superstore Sales Dashboard

## 📌 Project Overview

This project presents an interactive **Sales Dashboard** built using **Microsoft Power BI**. The dashboard analyzes the Sample Superstore dataset to provide valuable business insights through data visualization and storytelling.

The goal of this project is to help business stakeholders understand sales performance, profitability, customer segments, and regional trends using an easy-to-understand dashboard.

---

## 🎯 Objectives

- Analyze sales and profit performance.
- Identify the best-performing product categories.
- Understand regional sales distribution.
- Compare customer segments.
- Present business insights through interactive visualizations.

---

## 🛠️ Tools Used

- Microsoft Power BI
- Sample Superstore Dataset (CSV)

---

## 📂 Dataset

- **Dataset Name:** Sample Superstore
- **File Type:** CSV
- **Source:** Sample Superstore Dataset

---

## 📈 Dashboard Features

### KPI Cards
- Total Sales
- Total Profit
- Total Quantity
- Total Orders

### Visualizations
- Sales by Category
- Profit by Sub-Category
- Monthly Sales Trend
- Sales by Region
- Sales by Segment
- Profit by State (Map)

---

## 📊 Key Business Insights

- Technology generated the highest sales among all product categories.
- Copiers were the most profitable sub-category.
- The West region contributed the highest overall sales.
- Consumer customers accounted for the largest share of sales.
- Overall, the business demonstrated strong sales performance and positive profitability.

---

