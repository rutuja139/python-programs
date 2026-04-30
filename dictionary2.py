# Create an empty dictionary and display it
data = {}
print("Empty Dictionary:", data)

# Ask the user how many items to add
n = int(input("How many items do you want to add? "))

# Input key-value pairs
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

# Show the dictionary after adding items
print("Dictionary after adding items:", data)

# Ask the user to update a key's value
update_key = input("Enter key to update: ")
if update_key in data:
    new_value = input("Enter new value: ")
    data[update_key] = new_value
    print("Value updated")
else:
    print("Key not found")

# Retrieve and print a value using a key
search_key = input("Enter key to retrieve value: ")
if search_key in data:
    print("Value:", data[search_key])
else:
    print("Key not found")

# Use get() to retrieve a value
get_key = input("Enter key to retrieve using get(): ")
value = data.get(get_key)
if value is None:
    print("Key not found")
else:
    print("Value:", value)

# Delete a key-value pair
delete_key = input("Enter key to delete: ")
if delete_key in data:
    del data[delete_key]
    print("Deleted")
else:
    print("Key not found")

# Display the updated dictionary
print("Updated Dictionary:", data)
