def cal(marks, total_courses):
    if any(i <40 for i in marks):
        return "fail"
    total = sum(marks)
    aggregate_percent = ((total/total_courses*100))*100
    if aggregate_percent>75:
        grade = "distinction"
    elif 70<aggregate_percent<80:
        grade = "First Division"
    elif 60<aggregate_percent<70:
        grade = "Second Division"
    else:
        grade = "Third Division"
    return(aggregate_percent, grade)
total_courses = int(input("Enter number of courses: "))
marks = list(map(int,input().split()))
print(cal(marks, total_courses))
