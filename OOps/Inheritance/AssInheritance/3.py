class Employee:
    def  salary(self):
        pass
    

    
class Developer(Employee):
        def salary(self):
            print("Developer salary is 40000")

class Tester(Employee):
        def salary(self):
            print("Tester salary is 50000")

class HR(Employee):
     def salary(self):
          print("HR salary is 60000")


d=Developer()
d.salary()

t=Tester()
t.salary()

hr=HR()
hr.salary()
   
