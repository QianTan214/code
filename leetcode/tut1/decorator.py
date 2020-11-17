

import time
t1 = time.time()
t2= time.time()
print("Total time: {:.4} s," .format(t2 - t1))



# decorator

def display_time(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        print("Total time: {:.4} s," .format(t2 - t1)) # 保留四位小数
    return wrapper



# *args表示不知道有多少参数