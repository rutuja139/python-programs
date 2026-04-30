# Program to classify age group

age = int(input("enter age : "))   # Taking age as input

if age <= 5:
    print("toddler")

elif 5 < age <= 12:
    print("child")

elif 12 < age <= 18:
    print("teenager")

else:
    print("adult")
