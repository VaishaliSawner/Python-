"""4. Student Grade System
Problem
Create a student result management system.
Requirements
Each student should have:
roll number
name
marks in 3 subjects
Functionalities
Calculate total marks
Calculate percentage
Assign grade:
A → 90+
B → 75+
C → 50+
Fail otherwise
Track total students
Concepts Practiced
instance methods
conditional logic in classes
object-based calculations"""

class Student:
    count = 0
    def __init__(self,roll_no,name,marks):
        Student.count += 1
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
    def display(self):
        total = 0
        print("Student details = ")
        print(f"Roll no. = {self.roll_no}")
        print(f"Name = {self.name}")
        print(f"Marks = {self.marks}")
        for i in self.marks:
            total += i
        print(f"Total marks = {total}")
        percentage = total/3
        print(f"Percentage = {percentage}")
        if percentage > 90:
            print("Grade A")
        elif percentage > 75 and percentage<=90:
            print("Grade B")
        elif percentage > 50 and percentage <= 75:
            print("Grade C")
        else:
            print("Fail")
obj = Student(101,"Sanjana",[96,93,96])
obj.display()
obj1 = Student(102,"Tanishi",[78,96,78])
obj1.display()
print(f"Total Student = {Student.count}")