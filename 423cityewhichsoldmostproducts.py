import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)
# Group by City and calculate total quantity sold
city_sales = df.groupby('City')['Quantity'].sum()

# Find the city with the highest total quantity sold
best_city = city_sales.idxmax()
# write the code..

# Display the result
print(f"City sold the most products: {best_city}")
#ADD IN TERMINAL TO RUN: python "LAB7\frequentlysoldproductpairs424.py"
#add this to run: python "LAB7\cityewhichsoldmostproducts4.2.3.py"
