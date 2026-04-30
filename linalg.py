import numpy as np
A = np.array([[3, 1],[1, 2]])
b = np.array([9, 8])
solution = np.linalg.solve(A, b)
print("x =", solution[0])
print("y =", solution[1])

