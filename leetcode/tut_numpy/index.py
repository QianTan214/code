import numpy as np

a = np.arange(3,15)
print(a[3]) # 6

b = np.arange(3,15).reshape(3,4)
print(b[2]) # [11 12 13 14] 二维矩阵索引是一整行
print(b[1][1]) # 8 第一行第一列
print(b[1, 1]) # 8 第一行第一列
print(b[2,:]) # [11 12 13 14]
print(b[2:]) # [[11 12 13 14]]
print(b[:,1]) # [ 4  8 12]
print(b[1,1:3])# [8 9]

for row in b:
    print(row)
for col in b.T:
    print(col)

print(b.flatten())
for item in b.flat:
    print(item)