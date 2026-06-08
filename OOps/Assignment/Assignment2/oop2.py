class Bank_Account:
    interest_rate=5.0



    def __init__(self,acc_no,holder_name,balance):
        self.__acc_no=acc_no
        self.__holder_name=holder_name
        self.__balance=balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Amount {amount} deposited successfully")
        else:
            print("Invalid amount")

    def withdraw(self,amount):
         if Bank_Account.validate_balance(self.__balance,amount):
             self.__balance-=amount
             print(f"Amount {amount} withdrawn successfully")
         else:
             print("Insufficient balance or invalid amount")

    def displaySummary(self):
        print(f"Account No : {self.__acc_no}")
        print(f"Holder Name :{self.__holder_name}")
        print(f"Balance : {self.__balance}")
        print(f"Interest Rate : {Bank_Account.interest_rate}%")


    @staticmethod
    def validate_balance(balance,amount):
        minimum_balance=500
        if amount >0 and  balance-amount>=minimum_balance:  
            return True
        else:
            return False
        


acc1 =Bank_Account("12345","Atul",1000)
acc2 =Bank_Account("65732","John",1500)


acc1.deposit(500)
acc1.withdraw(200)
acc1.displaySummary()

acc2.deposit(1000)
acc2.withdraw(300)
acc2.displaySummary()