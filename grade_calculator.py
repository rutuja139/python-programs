# Program to assign grade based on marks

marks = int(input("enter marks : "))   # Taking marks as input

if marks < 40:
    print("F")

elif 40 < marks <= 60:
    print("C")

elif 60 < marks <= 80:
    print("B")

else:
    print("A")
