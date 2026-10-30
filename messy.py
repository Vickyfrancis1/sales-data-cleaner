import pandas as pd

data = {
    "name": ["Ada", "obi", "ZARA", "Emeka", "Ada"],
    "score": [72, None, 88, 40, 72],
    "city": ["Lagos", "Abuja", "lagos", None, "Lagos"],
}

table = pd.DataFrame(data)
print(table)
print(table.isna())
print(table.isna().sum())

table["name"] = table["name"].str.strip().str.title()
table["city"] = table["city"].str.strip().str.title()
table = table.drop_duplicates()
table = table.dropna(subset =["score"])
table["city"] = table["city"].fillna("Unknown")
print(table)
print(table["score"].mean())

