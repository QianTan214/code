class BankAccount:
    def __init__(self, accountNumber, accountName, balance): # constructor构造器
        self.accountNumber = accountNumber
        self.accountName = accountName
        self.balance = balance

    # 方法表示一种动作，表示这个class能做什么
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def withdraw(self, amount):
        self.balance = self.balance - amount

    def __str__(self): # 内置方法__str__
        return "(" + self.accountName + ": " + str(self.balance) + ")"

    def __lt__(self, other): # 内置方法__lt__表示less than
        return self.balance < other.balance

    def __gt__(self, other): # 内置方法__gt__表示greater than
        return self.balance > other.balance