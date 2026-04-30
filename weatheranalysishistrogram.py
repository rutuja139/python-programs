import matplotlib.pyplot as plt
import numpy as np

# Days
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Temperature data
temperature = [30, 32, 35, 33, 31, 29, 28]

# Rainfall data
rainfall = [5, 0, 2, 10, 8, 15, 20]

# Weather type
weather = ['Sunny', 'Cloudy', 'Rainy']
count = [3, 2, 2]

# Humidity vs temperature
temp = [28, 29, 30, 31, 32, 33, 35]
humidity = [80, 78, 75, 72, 70, 68, 65]



plt.figure()
plt.hist(temperature, bins=5)
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.show()
