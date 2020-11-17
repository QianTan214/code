from oop_bank import BankAccount

# 创建两个object b1, b2
b1 = BankAccount("12345", "Tom", 500)
b2 = BankAccount("56789", "Jerry", 150)

b1.withdraw(100)
b2.deposit(100)

# print(b1.balance)
# print(b2.balance)

# 通过设置__str__，直接打印object b1, b2
print(b1)
print(b2)

# 通过设置__lt__，直接比较object b1, b2
print(b1 < b2)

# 通过设置__gt__，直接比较object b1, b2
print(b1 > b2)