import pandas as pd

# Read the text file into a DataFrame
file = input()
data = pd.read_csv(file, sep="\s+", header=None, names=["Name", "Age", "Grade"])


# Display first five rows
print("First five rows:")
print(data.head())

# Calculate average age up to 2 decimal places
avg_age = round(data["Age"].mean(), 2)
print("Average age:", avg_age)

# Filter students with grade above B
filtered = data[data["Grade"] <= "B"]

print("Students with a grade up to B")
print(filtered)



