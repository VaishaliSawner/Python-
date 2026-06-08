from datetime import date

class Employee:
    def __init__(self, name, salary, hire_year):
        self.name = name
        self.salary = salary
        self.hire_year = hire_year

    def years_of_service(self):
        current_year = date.today().year
        return current_year - self.hire_year


e = Employee("Atul", 30000, 2020)
print("Years of Service:", e.years_of_service())