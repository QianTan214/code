import numpy as np

array = np.array([[1,2,3],[4,5,6]], dtype=np.float64) # float 32, 64

print(array)
print(array.dtype) # int64

print(array.ndim) # 2
print(array.shape) # (2, 3)
print(array.size) # 6

array1 = np.zeros((3,4))
array2 = np.ones((3,4), dtype= int)
array3 = np.empty((3,4))
array4 = np.arange(1,10,2) # 像python的range
array5 = np.arange(12).reshape(3,4)
array6 = np.linspace(1,10,5,dtype=int)
array7 = np.linspace(1,10,6).reshape(2,3)

print(array1)
print(array2)
print(array3)
print(array4)
print(array5)
print(array6)
print(array7)

