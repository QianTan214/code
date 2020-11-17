import numpy as np

a = np.arange(12).reshape(3,4)
print(a)
print(np.split(a,2,axis = 1))
print(np.split(a,3,axis = 0)) # [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
# print(np.split(a,3,axis = 1)) # 会报错，不等量分隔
print(np.array_split(a,3,axis = 1)) # 不等量分隔
print(np.vsplit(a,3)) 
print(np.hsplit(a,2)) 
