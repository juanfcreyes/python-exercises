class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print('Sorry, minimum balance must be maintained.')
        else:
            BankAccount.withdraw(self, amount)

a = BankAccount()
b = BankAccount()
a.deposit(100)
print("a:" + str(a.balance))
b.deposit(50)
print("b:" + str(b.balance))
b.withdraw(10)
print("b:" + str(b.balance))
a.withdraw(10)
print("a:" + str(a.balance))




