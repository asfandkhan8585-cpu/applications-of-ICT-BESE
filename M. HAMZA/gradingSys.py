#Relational A

marks = int(input("Enter your marks"))

if marks >= 90:
    grade = "A+"
elif  marks >= 75:
    grade ="B"
elif marks >= 60:
    grade = "C"
elif marks >= 30:
    grade = "D"
elif marks < 30:
    grade = "F"
else: 
    print("Invalid Input")

print("Your Grade is : " , grade)