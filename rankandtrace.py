import numpy as np
A = np.array([[1, 2], [2, 4]])
rank = np.linalg.matrix_rank(A)
trace = np.trace(A)
print("Rank:", rank)
print("Trace:", trace)