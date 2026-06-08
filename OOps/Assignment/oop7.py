class Account:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, acc_no):
        self.accounts = [acc for acc in self.accounts if acc.acc_no != acc_no]

    def display(self):
        for acc in self.accounts:
            print(acc.acc_no, acc.name, acc.balance)



b = Bank()
a1 = Account(101, "Atul", 5000)
a2 = Account(102, "Rahul", 3000)

b.add_account(a1)
b.add_account(a2)

a1.deposit(1000)
a2.withdraw(500)

b.display()