import math   # Importing math module for mathematical functions

n = int(input("enter a number : "))   # Taking number as input

if 0 < n < 10:
    print(n**2)   # Printing square of number

elif 10 < +n < 100:
    print(math.sqrt(n))   # Printing square root of number

elif 100 <= n < 1000:
    print(math.cbrt(n))   # Printing cube root of number

else:
    print("invalid")   # If number does not match any condition
