from dao.employee_dao import EmployeeDAO
from model.emnployee


while True:
    print("Press 1 for insertion ")
    print("Press 0 for exit")
    choice = int(input("Enter your choice"))
    if choice==1:
        name=input("Enter your name:")
        salary=input("Enter the salary")
        department=input("Enter the department")
