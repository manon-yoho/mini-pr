import pandas as pd

import matplotlib.pyplot as plt

import os

data = [
    {
        "Model": "Sedan A",
        "Price_Lakhs": 12.5,
        "Units_Sold": 45,
        "Rating": 4.2,
    },
    {
        "Model": "SUV B",
        "Price_Lakhs": 18.2,
        "Units_Sold": 30,
        "Rating": 4.5,
    },
    {
        "Model": "Hatchback C",
        "Price_Lakhs": 8.0,
        "Units_Sold": 65,
        "Rating": 3.8,
    },
    {
        "Model": "EV D",
        "Price_Lakhs": 15.0,
        "Units_Sold": 20,
        "Rating": 4.7,
    },
    {
        "Model": "Sedan E",
        "Price_Lakhs": 21.0,
        "Units_Sold": 15,
        "Rating": 4.6,
    },
]

df = pd.DataFrame(data)
print(df)

df.to_csv('car_data.csv', index=False)


plt.figure(figsize=(8, 6))
plt.bar(df['Model'], df['Units_Sold'], color='skyblue')
plt.title('Monthly Car Sales by Model')
plt.xlabel('Car Model')
plt.ylabel('Units Sold')
plt.grid(axis='y', linestyle='--', alpha=0.7)
os.makedirs('reports/figures', exist_ok=True)
plt.savefig('reports/figures/car_sales_bar.png')
plt.show()

# Histogram: 
plt.figure(figsize=(
    8,
    6,
))
plt.hist(
    df['Price_Lakhs'], bins=4, color='skyblue', edgecolor='black'
)
plt.title('Distribution of Car Prices')
plt.xlabel('Price in Lakhs (INR)')
plt.ylabel('Number of Models')
plt.grid(axis='y', linestyle='--', alpha=0.7)
os.makedirs('reports/figures', exist_ok=True)
plt.savefig('reports/figures/car_price_hist.png')
plt.show()

# Scatter Plot: 
plt.figure(
    figsize=(8, 6)
)
plt.scatter(
    df["Price_Lakhs"], df["Units_Sold"], color="skyblue", s=100
)
plt.title("Price vs. Units Sold")
plt.xlabel("Price in Lakhs (INR)")
plt.ylabel("Units Sold")
plt.grid(True, linestyle="--", alpha=0.7)
os.makedirs("reports/figures", exist_ok=True)
plt.savefig("reports/figures/car_scatter.png")
plt.show()