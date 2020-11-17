import numpy as np

a = np.array([1,1,1])
b = np.array([2,2,2])
c = np.vstack((a,b))
d = np.hstack((a,b)) 


print(c)
print(a.shape, c.shape) # (3,) (2,3)
print(d) # [1 1 1 2 2 2]
print(a.shape, d.shape) # (3,) (6,)


print(a.T) # [1 1 1] 不能把序列Transpose
print(a[np.newaxis,:]) # [[1 1 1]] 
print(a[:, np.newaxis]) 
"""
[[1]
 [1]
 [1]]
"""


e = np.array([1,1,1])[:,np.newaxis]
f = np.array([2,2,2])[:,np.newaxis]
print(np.vstack((e,f)))
print(np.hstack((e,f)))
g = np.concatenate((e,f,f), axis = 1) # 多个array合并， axis = 1左右，axis = 0上下
print(g)