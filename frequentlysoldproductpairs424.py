import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()


# Read data from the specified CSV file
df = pd.read_csv(file_name)
grouped = df.groupby('Date')['Product'].apply(list)

# Count all product pairs
pair_counter = Counter()

for products in grouped:
    pairs = combinations(sorted(products), 2)
    pair_counter.update(pairs)

# Find the highest frequency
max_count = max(pair_counter.values())

# Get all pairs with highest frequency
most_frequent_pairs = [pair for pair, count in pair_counter.items() if count == max_count]

# Output the most frequent product pairs
for pair in most_frequent_pairs:
    print(f"{pair[0]} and {pair[1]}: {max_count} times")
