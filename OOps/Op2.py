# CONSTRUCTOR with argument 

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

s1 = Student("Atul", 25)
s2 = Student("Rahul", 30)
s1.display()
s2.display()