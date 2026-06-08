class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)

    def display(self):
        print(self.name, self.grade, self.courses)


s = Student("Atul", "A")
s.add_course("Math")
s.add_course("Python")

s.display()

s.remove_course("Math")
s.display()