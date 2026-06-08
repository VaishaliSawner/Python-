class Employee:
    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.salary = salary

    def update_salary(self, amount):
        self.salary += amount

    def display(self):
        print(f"{self.name} , {self.job} ,{self.salary}")


e = Employee("Atul", "Developer", 30000)

e.display()
e.update_salary(5000)
e.display()