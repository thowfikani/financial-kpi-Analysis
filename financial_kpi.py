import pandas as pd

# Create the dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Revenue": [500000, 550000, 600000, 620000, 650000, 700000],
    "Expenses": [300000, 320000, 340000, 360000, 370000, 390000],
    "Marketing Cost": [60000, 65000, 70000, 72000, 75000, 80000],
    "New Customers": [200, 220, 250, 260, 280, 300],
    "Avg Revenue/Customer": [2500, 2500, 2500, 2500, 2500, 2500],
    "Customer Lifetime": [3, 3, 3, 3, 3, 3]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate KPIs
df["Burn Rate"] = df["Expenses"]
df["CAC"] = df["Marketing Cost"] / df["New Customers"]
df["LTV"] = df["Avg Revenue/Customer"] * df["Customer Lifetime"]
df["LTV:CAC"] = df["LTV"] / df["CAC"]
df["Run Rate"] = df["Revenue"] * 12

print("Financial KPI Dataset")
print(df)
