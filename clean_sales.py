import pandas as pd

table = pd.read_excel("messy_sales.xlsx")

table["Item"] = table["Item"].str.strip().str.title()
table["Category"] = table["Category"].str.strip().str.title()

table = table.drop_duplicates()
table = table.dropna(subset=["Item"])
table["Total"] = table["Qty"] * table["Price"]

summary = table.groupby("Category")["Total"].sum()
summary = summary.rename("Total Sales (NGN)")
summary.to_excel("sales_report.xlsx")
table.to_excel("sales_clean.xlsx", index=False, na_rep="Missing")
print("Report saved: sales_report.xlsx")
print("Report saved: sales_report.xlsx and sales_clean.xlsx")

