"""2. Bank Account Simulation
Problem
Design a banking system using OOP.
Requirements
Each account should contain:
account number
holder name
balance
Functionalities
Deposit money
Withdraw money
Prevent withdrawal if balance insufficient
Display account summary
Maintain bank-wide interest rate as class variable
Add static method to validate minimum balance rule
Concepts Practiced
object state management
static methods
class variables
validations"""

class Bank:
    def __init__(self,acc_no,hol_name,balance):
        self.acc_no = acc_no
        self.hol_name = hol_name
        self.balance = balance

    @staticmethod
    def min_balance(balance):
        if balance > 0:
            return True
        return False

    def dep_money(self,money):
        if Bank.min_balance(money):
            self.balance += money
            print(f"Your new balance = {self.balance} after deposite {money} RS")
        else:
            print("Amount must be greater than 0")
    
    def with_money(self,money):
        if Bank.min_balance(money):
            if (self.balance - money) > 500:
                self.balance -= money
                print(f"Your new balance = {self.balance} after withdraw {money} RS")
            else:
                print(f"Insuffient balance for withdraw")
                print(f"Your balance = {self.balance}")
        else:
            print("Withdraw amount must be greater than 0")

    def display(self):
           print("Account details:")
           print(f"Account No. : {self.acc_no}")
           print(f"Holder Name:{self.hol_name}")
           print(f"Balance :{self.balance}")
obj = Bank("SBI348954","Sanjana",500)
obj.display()
obj.dep_money(200)
obj.with_money(300)