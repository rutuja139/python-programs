import numpy as np
# Step 1: Coefficient matrix (items count)
# 2 apples + 1 milk
# 1 apple  + 3 milk

A = np.array([[2, 1], [1, 3]])

# Step 2: Total prices
b = np.array([70, 110])

# Step 3: Solve for prices
prices = np.linalg.solve(A, b)
# Step 4: Extract values
apple_price = prices[0]
milk_price = prices[1]

# Step 5: Print results
print("Price of 1 apple: ₹", apple_price)
print("Price of 1 milk: ₹", milk_price)

