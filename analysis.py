import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("sales.db")

query = """
SELECT strftime('%Y-%m', order_date) AS month,
       SUM(o.quantity * p.price) AS revenue
FROM orders o
JOIN products p ON o.product_id = p.id
GROUP BY month
ORDER BY month
"""

df = pd.read_sql(query, conn)

print(df)

df.to_csv("monthly_revenue.csv", index=False)

plt.figure()
plt.plot(df["month"], df["revenue"])
plt.title("Monthly Revenue")
plt.savefig("monthly_revenue.png")

conn.close()
