physics=int(input("Enter the marks"))
Chemistry=int(input("Enter the marks"))
Biology=int(input("Enter the marks"))
Mathematics=int(input("Enter the marks"))
Computer=int(input("Enter the marks"))
Total_marks=physics+Chemistry+Biology+Mathematics+Computer

per=(Total_marks/500)*100

print(per)

if(per>=90):
    print("Grade A")
elif(per>=80):
    print("Grade B")
elif(per>=70):
    print("Grade C")
elif(per>=60):
    print("Grade D")
elif(per>=40):
    print("Grade E")
else:
    print("F")