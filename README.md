# Sales Analysis Project (SQL + Python)

Mini data analytics project combining SQLite and Python.

## 📌 Description

This project demonstrates:

- relational database design (SQLite)
- SQL joins & aggregations
- Python data analysis with pandas
- visualization with matplotlib

The pipeline:

SQLite → SQL queries → pandas → CSV report → chart

## 🧱 Database Schema

Tables:

- customers
- products
- orders

## 📊 Analysis

Monthly revenue is calculated using SQL joins and aggregation.

Output:

- monthly_revenue.csv
- monthly_revenue.png

## ⚙️ Tech Stack

- Python 3
- SQLite
- pandas
- matplotlib

## ▶️ How to Run

```bash
python -m venv venv
venv\Scripts\activate
pip install pandas matplotlib
python analysis.py
