# Taking two numbers as input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Taking operator as input
operator = input("Enter operator: ")

# Performing calculation based on operator
if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    print("Result:", num1 / num2)
    
else:
    print("Invalid operator entered.")
