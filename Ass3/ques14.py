marks = float(input("Enter percentage: "))

if marks > 90:
    grade = "A"
elif marks > 80:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)