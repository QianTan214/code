# append用法：

s1 = [1,2,3]
s2 = [4]
s1.append(s2)
s1.append({'1':'2'})
print(s1)

输出如下

[1,2,3,[4],{'1':'2'}]



# +运算：
s1 = [1,2,3]
s2 = [4]
print(s1+s2)

结果如下

[1,2,3,4]


# extend用法:
s1 = [1,2,3]
s2 = [4]
s1.extend(s2)
print(s1)
s3 = 'abc'
s1.extend(s3))
print(s1)
s4 = {'age':12,'height':180}
s1.extend(s4)
print(s1)

输出如下：

[1, 2, 3, 4]
[1, 2, 3, 4, 'a', 'b', 'c']
[1, 2, 3, 4, 'a', 'b', 'c', 'height', 'age']