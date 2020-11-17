class A:
    def __init__(self):
        self.a = 1
        self.b = 2

    def __hash__(self):
        return hash(str(self.a) + str(self.b))

a = A()
print(hash(a))

"""
结果： -1660634806518362315 (每次hash结果不一样)

"""