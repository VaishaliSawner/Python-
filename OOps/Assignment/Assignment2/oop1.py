
'''
1. Employee Management System
Problem

Create an Employee class to manage employee details.

Requirements

Each employee should have:

employee id
name
department
salary
Functionalities
Display employee details
Increase salary by percentage
Count total employees created using a class variable

Create employee object from a string:

"101-Atul-IT-50000"

Employee 
  Property- (id,name,department,salary)
  Behaviour :- display(self),increase_salary(self,percentage)

__new__ :- create the object in python  

__ [private]
_ [protect]

'''

class Employee:

    def __init__(self,id,name,department,salary):
        self.__id=id
        self.__name=name
        self.__department=department
        self.__salary=int(salary)

    def display(self):
        print(f"Id : {self.__id}\nName:")




        e1 = Employee("101-Atul-IT-50000")
        e1.display()


























































class Employee:
    count=0
    def __init__(self, employee_id, name, department, salary):
        Employee.count += 1
        self.__employee_id = employee_id
        self.__name = name
        self.__department = department
        self.__salary = salary
    

    def display(self):
        print(f"Employee ID: {self.__employee_id}, Name: {self.__name}, Department: {self.__department}, Salary: {self.__salary}")

    def increase_salary(self,percentage):
        increment=self.__salary*percentage/100
        self.__salary+=increment
        print(f"Salary increased by {percentage}%")
        print(f"New salary:{self.__salary}")


e1=Employee(101,"Atul","IT",50000)
e2=Employee(102,"Rahul","HR",60000)
e3=Employee(103,"Rohit","Finance",70000)
e1.display()
e2.display()
e3.display()
print(f"Total employees: {Employee.count}")

e1.increase_salary(5)
e2.increase_salary(10)
e3.increase_salary(15)
