import pandas as pd

# Provided dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Adding a new row
name = input("New name: ")
age=int(input("New age: "))
df.loc[len(df)] = [name,age]
# Display the DataFrame after adding a new row
print("After adding a row:\n",df)

# Modifying a row
index = int(input("Index of row to modify: "))
new_age = int(input("New age: "))
df.loc[index,'Age'] = new_age
# Display the DataFrame after modifying a row
print("After modifying a row:")
print(df)

# Deleting a row
delete_index = int(input("Index of row to delete: "))
df = df.drop(delete_index).reset_index(drop=True)
# Display the DataFrame after deleting a row
print("After deleting a row:")
print(df)

# Adding a new column
gender_values = input("Enter genders separated by space: ").split()
df['Gender'] = gender_values
# Display the DataFrame after adding a new column
print("After adding a new column:")
print(df)

# Modifying a column
df['Name']=df['Name'].str.upper()
# Display the DataFrame after modifying a column
print("After modifying a column:")
print(df)

# Deleting a column
df = df.drop(columns=['Age']).reset_index(drop=True)
# Display the DataFrame after deleting a column
print("After deleting a column:")
print(df)
