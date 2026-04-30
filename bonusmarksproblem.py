import numpy as np

marks = np.array([55,65,75,85,95])

new_marks = marks + 5

print("New Marks:", new_marks)
print("Average:", np.mean(new_marks))
print("Highest:", np.max(new_marks))