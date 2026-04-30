# Program to calculate aggregate percentage and grade

courses = int(input("Enter number of courses: "))   # Number of subjects
total = 0
fail = False

for i in range(courses):
    marks = int(input("Enter marks: "))
    
    if marks < 40:   # Check if any subject is failed
        fail = True
    
    total += marks   # Adding marks to total

percentage = total / courses   # Calculating aggregate percentage

print("Aggregate Percentage:", percentage)

if fail:
    print("Fail")
else:
    if percentage >= 75:
        print("Grade: A")
    elif percentage >= 60:
        print("Grade: B")
    elif percentage >= 50:
        print("Grade: C")
    else:
        print("Grade: D")
