import numpy as np

a = np.array ([10,20,30,40])
b = np.arange(4)
e = np.array([[1,1],[0,1]])
f = np.arange(4).reshape(2,2)
g = e * f # 点乘 

c = a - b
d = 10 * np.sin(a)

print(c)
print(b**2)
print(d)
print(b<3)

print(g)
print(np.dot(e,f)) # 矩阵相乘
print(e.dot(f)) # 矩阵相乘

h = np.random.random((2,4))
print(h)
print(np.sum(h, axis = 1)) # axis = 1 行
print(np.max(h, axis = 0)) # axis = 0 列

