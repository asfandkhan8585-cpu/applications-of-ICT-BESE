marks = int(input("enter your marks="))

if marks >= 90:
    grade = "A"

elif marks >=75:
    grade = "B"

elif marks >=60:
    grade = "C"

elif marks >=40:
    grade = "d"

else:
    print("invalid output")
print("your grade is=",grade)  