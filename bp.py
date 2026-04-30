import numpy as np
morning = np.array([[120, 125, 130],[110, 115, 120],[130, 135, 140]])
evening = np.array([[130, 128, 135],[118, 120, 125],[140, 138, 145]])
daily_avg = np.mean(morning, axis=0)
print("Daily Average BP (Morning):", daily_avg)
difference = evening - morning
print("\nBP Difference:\n", difference)
high_increase = difference > 10
print("\nIncrease > 10:\n", high_increase)
combined_effect = morning * evening
print("\nCombined Effect:\n", combined_effect)
max_bp = np.max(evening)
print("\nMaximum BP Recorded:", max_bp)