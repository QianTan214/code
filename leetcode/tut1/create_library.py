# import math
# 用help('math')查看math库里有哪些function

# 我们可以自己创建库
# 然后用import create_library和help("create_library")查看

# python create_library.py -v来查看测试结果


"""
This is my own library.
"""
def add(a, b):

    """
    calculate sum of a and b
    >>> add(1, 1)
    2
    >>> add(2, 3)
    5
    """
    return a + b


def subtract(a, b):

    """
    calculate substraction of a and b
    >>> subtract(1, 1)
    0
    >>> subtract(2, 3)
    -1
    """
    
    return a - b

# 加下面这段话
if __name__ == '__main__':
    import doctest
    doctest.testmod()

