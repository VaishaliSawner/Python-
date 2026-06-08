class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


p1 = Person("Atul", 20)
p2 = Person("Rahul", 22)

p1.display()
p2.display()