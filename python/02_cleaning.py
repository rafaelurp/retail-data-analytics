import pandas as pd
input_path = "../data/raw/online_retail.csv"
output_path = "../data/processed/retail_clean.csv"

df = pd.read_csv(input_path, encoding="latin1")

print("Registros iniciales:", df.shape[0])

df = df.dropna(subset=["CustomerID"])
print("Después de eliminar CustomerID nulo:", df.shape[0])

df = df[df["Quantity"] > 0]
print("Después de eliminar devoluciones:", df.shape[0])

df = df[df["UnitPrice"] > 0]

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["CustomerID"] = df["CustomerID"].astype(int)

df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

df = df.sort_values(by="InvoiceDate")

df.to_csv(output_path, index=False)

print("Archivo limpio generado correctamente")
