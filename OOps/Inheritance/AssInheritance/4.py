class Person:
    def show(self):
        pass

class Student(Person):
    def study(self):
        print("I am a student")

class Teacher(Person):
    def teach(self):
        print("I am  a teacher")

s=Student()
s.study()

t=Teacher()
t.teach()