class Foo:
    def __init__(self,name):
        self.name=name

    def __getitem__(self, item):
        print(self.__dict__[item])

    def __setitem__(self, key, value):
        print(key,value)
        self.__dict__[key] = value

    def __delitem__(self, key):
        print('__delitem__ obj[key]时,我执行')
        self.__dict__.pop(key)

    def __delattr__(self, item):
        print('__delattr__ obj.key时,我执行')
        self.__dict__.pop(item)

obj = Foo('sb')

print("--setitem----执行------")
obj['age'] = 18

print("--getitem----执行------")
obj['age']

print("--delitem----执行------")
del obj['age']
# obj['age']


obj['name'] = 'alex'
print(obj.__dict__)

print("--delattr----执行------")
del obj.name
# obj["name"]