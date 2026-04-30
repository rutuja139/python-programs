from datetime import datetime

birth_input = input("Enter birthdate (DD-MM-YYYY): ")
salary_inr = float(input("Enter salary in INR: "))

birthdate = datetime.strptime(birth_input, "%d-%m-%Y")
today = datetime.today()

age = today.year - birthdate.year
if (today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1

salary_usd = salary_inr / 83

print("Age:", age)
print("Salary in USD: {:.2f}".format(salary_usd))
