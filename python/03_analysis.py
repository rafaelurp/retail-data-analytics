import pandas as pd

input_path = "../data/processed/retail_clean.csv"
df = pd.read_csv(input_path)

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

total_sales = df["TotalAmount"].sum()
total_orders = df["InvoiceNo"].nunique()
total_customers = df["CustomerID"].nunique()

print("Ventas totales:", round(total_sales, 2))
print("Total pedidos:", total_orders)
print("Clientes únicos:", total_customers)

average_ticket = total_sales / total_orders
print("Ticket promedio:", round(average_ticket, 2))

df["YearMonth"] = df["InvoiceDate"].dt.to_period("M")

sales_by_month = (
    df.groupby("YearMonth")["TotalAmount"]
    .sum()
    .reset_index()
)

sales_by_country = (
    df.groupby("Country")["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

top_customers = (
    df.groupby("CustomerID")["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

top_products = (
    df.groupby(["StockCode", "Description"])["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

sales_by_month.to_csv("../data/processed/sales_by_month.csv", index=False)
sales_by_country.to_csv("../data/processed/sales_by_country.csv", index=False)
top_customers.to_csv("../data/processed/top_customers.csv", index=False)
top_products.to_csv("../data/processed/top_products.csv", index=False)
