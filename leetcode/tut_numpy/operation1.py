import numpy as np

a = np.arange(2,14).reshape(3,4)
print(np.argmin(a)) # 最小值索引
print(np.argmax(a)) # 最小值索引
print(a.mean())
print(np.mean(a))
print(np.median(a))
print(np.cumsum(a)) # [ 2  5  9 14 20 27 35 44 54 65 77 90] 累加
print(np.diff(a)) # 累差
"""
[[1 1 1]
 [1 1 1]
 [1 1 1]]
"""
print(np.nonzero(a))
print(np.transpose(a))
print(a.T) # transpose
print((a.T).dot(a))
print(np.clip(a,5,9)) # 小于5的都变5，大于9的都变9



b = np.arange(14,2,-1).reshape(3,4)
print(np.sort(b))

