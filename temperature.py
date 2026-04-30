temperatures = (30, 32, 29, 35, 31, 28,33)
print("Temperatures recorded during the week:")
for temp in temperatures:
    print(temp, "°C")
total_temp = sum(temperatures)
average_temp = total_temp / len(temperatures)
print("\nTotal Temperature:", total_temp)
print("Average Temperature:", average_temp)
highest_temp = max(temperatures)
lowest_temp = min(temperatures)
print("\nHighest Temperature:", highest_temp)
print("Lowest Temperature:", lowest_temp)
below_avg_count = 0
for temp in temperatures:
    if temp < average_temp:
        below_avg_count += 1
print("\nNumber of days below average temperature:", below_avg_count)