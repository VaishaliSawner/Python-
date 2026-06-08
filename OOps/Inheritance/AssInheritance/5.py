
class BankAccount:
    def withdrawalRules(self):
        pass

class SavingsAccount(BankAccount):
    def withdrawalRules(self):
        print("Must have 1000 rupees ")

class CurrentAccount(BankAccount):
    def withdrawalRules(self):
        print("Must have 500 rupees")


s=SavingsAccount()
s.withdrawalRules()

c=CurrentAccount()
c.withdrawalRules()

