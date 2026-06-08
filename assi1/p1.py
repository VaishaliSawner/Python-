'''1. Employee Management System Problem
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
Count total employees created using a class variable'''


class employee:
    def __init__(self,empId, name, depart, salary):
        self.__empId=empId
        self.__name=name
        self.__depart=depart
        self.__salary=salary
        
    def display(self):
        print(f"emp Id:{self.__empId},emp name:{self.__name}, department name{self.__depart}, salry:{self.__salary}")
     
    def increment(self):
        self.__salary=self.__salary+((20*self.__salary/100))
        print(f"salary after increment:{self.__salary}")
    
    @classmethod
    def from_string(cls, input_string):
        id, name, department, salary = input_string.split("-")
        return cls(id, name, department, float(salary))
    
    
# s1=employee(1,"Rupesh","IT",20000)
s1=employee.from_string("101-Rahul-IT-50000")
s1.display()
s1.increment()