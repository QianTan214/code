""" 三个双引号或单引号"""

# 以三个双引号或单引号开头的字符串可以折行
s3 = '''
hello, 
world!
'''
print(s3, end='')

提示：print函数中的end=''表示输出后不换行，
即将默认的结束符\n（换行符）更换为''（空字符）。



"""转义字符"""
s1 = '\'hello, world!\'' # 'hello, world!'
print(s1)
s2 = '\\hello, world!\\' # \hello, world!\
print(s2)
s3 = '\'hello, world!'   # 'hello, world!
print(s3)



"""原始字符串"""
# 字符串s1中\t是制表符，\n是换行符
s1 = '\time up \now'
print(s1)
# 字符串s2中没有转义字符，每个字符都是原始含义
s2 = r'\time up \now'
print(s2)



"""十六进制八进制"""

Python中还允许在\后面还可以跟一个八进制或者十六进制数来表示字符，
例如\141和\x61都代表小写字母a，前者是八进制的表示法，后者是十六进制的表示法。
另外一种表示字符的方式是在\u后面跟Unicode字符编码，
例如\u9a86\u660a代表的是中文“骆昊”。运行下面的代码，看看输出了什么。

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)



"""is 和 ="""
s1 = 'hello world'
s2 = 'hello world'
s3 = s2
# 比较字符串的内容
print(s1 == s2, s2 == s3)    # True True
# 比较字符串的内存地址
print(s1 is s2, s2 is s3)    # False True

""" string slicing"""
s = 'abc123456'

# i=2, j=9, k=2的正向切片操作
print(s[2::2])      # c246

# i=-7, j=9, k=2的正向切片操作
print(s[-7::2])     # c246

# i=0, j=9, k=2的正向切片操作
print(s[::2])       # ac246

# i=1, j=-1, k=2的正向切片操作
print(s[1:-1:2])    # b135

# i=7, j=1, k=-1的负向切片操作
print(s[7:1:-1])    # 54321c

# i=-2, j=-8, k=-1的负向切片操作
print(s[-2:-8:-1])  # 54321c

# i=7, j=-10, k=-1的负向切片操作
print(s[7::-1])     # 54321cba

# i=-1, j=1, k=-1的负向切片操作
print(s[:1:-1])     # 654321c

# i=0, j=9, k=1的正向切片
print(s[:])         # abc123456

# i=0, j=9, k=2的正向切片
print(s[::2])       # ac246

# i=-1, j=-10, k=-1的负向切片
print(s[::-1])      # 654321cba

# i=-1, j=-10, k=-2的负向切片
print(s[::-2])      # 642ca



"""find/index"""

s = 'hello, world!'


print(s.find('or'))        # 8
# 找不到返回-1
print(s.find('shit'))      # -1

print(s.index('or'))       # 8
# 找不到引发异常
print(s.index('shit'))     # ValueError: substring not found


在使用find和index方法时还可以通过方法的参数来指定查找的范围，
也就是查找不必从索引为0的位置开始。find和index方法还有逆向查找（从后向前查找）的版本，
分别是rfind和rindex，代码如下所示。

s = 'hello good world!'

# 从前向后查找字符o出现的位置(相当于第一次出现)
print(s.find('o'))       # 4
# 从索引为5的位置开始查找字符o出现的位置
print(s.find('o', 5))    # 7
# 从后向前查找字符o出现的位置(相当于最后一次出现)
print(s.rfind('o'))      # 12




"""startswith / endswith"""

s1 = 'hello, world!'

print(s1.startswith('He'))    # False
print(s1.startswith('hel'))   # True
print(s1.endswith('!'))       # True

s2 = 'abc123456'

print(s2.isdigit())    # False
print(s2.isalpha())    # False
print(s2.isalnum())    # True




"""格式化字符串"""

在Python中，字符串类型可以通过center、ljust、rjust
方法做居中、左对齐和右对齐的处理。

s = 'hello, world'

# center方法以宽度20将字符串居中并在两侧填充*
print(s.center(20, '*'))  # ****hello, world****
# rjust方法以宽度20将字符串右对齐并在左侧填充空格
print(s.rjust(20))        #         hello, world
# ljust方法以宽度20将字符串左对齐并在右侧填充~
print(s.ljust(20, '~'))   # hello, world~~~~~~~~