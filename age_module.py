from datetime import datetime
birth_year = int(input("enter your birth year: "))
current_year = datetime.now().year
age = current_year - birth_year
print("age :",age)