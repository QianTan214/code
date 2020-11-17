a = 1.736
res = round(a, 2)
print(res) # 结果1.74,四舍五入

# help(round)

# function 里没有return，默认是None
# return 可以返回多个值，用逗号隔开 如return a, b,默认返回tuple(a,b)
# 用type查看数据类型
# 序列解包：用变量接收return返回结果 c, d = func(a, b)，不要用索引index的方式

d = 1, 2, 3
print(type(d)) # tuple

"""
- 关键字参数，调用时可以不按形参顺序写，但必须写在必须参数后面
- 调用时add (y=3, x=3)
- 定义时可以有默认参数(default argument) def students(name, gender = "Male"),
  调用时只需写name就可以了，gender默认男
- 必须参数必须在默认参数前面
- 传参数时要按顺序，如需要跳过，则必须指明。如age = 17

"""



设置递归允许的最大次数，默认大概1000
- import sys
- sys.setrecursionlimit(3000)


pass 占位

if后的子语句封装成函数，使其变得更简洁易读


