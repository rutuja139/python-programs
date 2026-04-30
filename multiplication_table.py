# Program to print multiplication table

num = int(input("Enter a number: "))   # Taking number as input

for i in range(1, 11):   # Loop from 1 to 10
    print(num, "x", i, "=", num * i)
