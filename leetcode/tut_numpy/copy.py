import numpy as np

a = np.array([1,2,3,4])

b = a
c = a
d = a
a[0] = 11
print(a,b,c,d) # [11  2  3  4] [11  2  3  4] [11  2  3  4] [11  2  3  4]
print(b is a) # True

d[1:3] = (22,33)
print(a,b,c,d) # [11 22 33  4] [11 22 33  4] [11 22 33  4] [11 22 33  4]

e = a.copy() # deepcopy
print(e)
e[1] = 66
print(a, e) # [11 22 33  4] [11 66 33  4]