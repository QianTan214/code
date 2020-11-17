import numpy as np
import pandas as pd

s = pd.Series([1,3,6,np.nan,44,1])
print(s)
""" 
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
"""

dates = pd.date_range("20160101",periods = 6)
print(dates)
"""
DatetimeIndex(['2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04',
               '2016-01-05', '2016-01-06'],
              dtype='datetime64[ns]', freq='D')
"""

df = pd.DataFrame(np.random.rand(6,4), index = dates, columns= ["a","b","c","d"])
print(df)
"""
                   a         b         c         d
2016-01-01  0.736461  0.993865  0.532916  0.139806
2016-01-02  0.029150  0.304719  0.967294  0.719473
2016-01-03  0.245251  0.611637  0.170378  0.106227
2016-01-04  0.609279  0.827703  0.938939  0.098023
2016-01-05  0.747285  0.348712  0.717849  0.367898
2016-01-06  0.869212  0.642141  0.406003  0.695596
"""

df1 = pd.DataFrame(np.arange(12).reshape(3,4))
print(df1)
"""
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
"""

df2 = pd.DataFrame({"A":1,
"B":pd.Timestamp("20200101"),
"C":pd.Series(1,index = list(range(4)),dtype = 'float32'),
"D":np.array([3]*4,dtype = 'int32'),
"E":pd.Categorical(["test","train","test","train"]),
"F":"foo"
})

print(df2)

"""
   A          B    C  D      E    F
0  1 2020-01-01  1.0  3   test  foo
1  1 2020-01-01  1.0  3  train  foo
2  1 2020-01-01  1.0  3   test  foo
3  1 2020-01-01  1.0  3  train  foo
"""

print(df2.dtypes)
"""
A             int64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
"""

print(df2.index)
"""
Int64Index([0, 1, 2, 3], dtype='int64')
"""

print(df2.columns)
"""
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
"""

print(df2.values)
"""
[[1 Timestamp('2020-01-01 00:00:00') 1.0 3 'test' 'foo']
 [1 Timestamp('2020-01-01 00:00:00') 1.0 3 'train' 'foo']
 [1 Timestamp('2020-01-01 00:00:00') 1.0 3 'test' 'foo']
 [1 Timestamp('2020-01-01 00:00:00') 1.0 3 'train' 'foo']]
"""

print(df2.describe())
"""
         A    C    D
count  4.0  4.0  4.0
mean   1.0  1.0  3.0
std    0.0  0.0  0.0
min    1.0  1.0  3.0
25%    1.0  1.0  3.0
50%    1.0  1.0  3.0
75%    1.0  1.0  3.0
max    1.0  1.0  3.0
"""

# print(df2.T)

print(df2.sort_index(axis = 0, ascending = False))
"""
   A          B    C  D      E    F
3  1 2020-01-01  1.0  3  train  foo
2  1 2020-01-01  1.0  3   test  foo
1  1 2020-01-01  1.0  3  train  foo
0  1 2020-01-01  1.0  3   test  foo
"""

print(df2.sort_values(by = "E"))
"""
   A          B    C  D      E    F
0  1 2020-01-01  1.0  3   test  foo
2  1 2020-01-01  1.0  3   test  foo
1  1 2020-01-01  1.0  3  train  foo
3  1 2020-01-01  1.0  3  train  foo
"""