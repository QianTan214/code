# import time


# def display(num):
#     time.sleep(1)
#     print(num)


# for num in range(10):
#     display(num)

"""
上面这段代码相信大家很容看懂，程序会输出0到9的数字，每隔1秒中输出一个数字，
因此整个程序的执行需要大约10秒时间。值得注意的是，因为没有使用多线程或多进程，
程序中只有一个执行单元，而time.sleep(1)的休眠操作会让整个线程停滞1秒钟，
对于上面的代码来说，在这段时间里面CPU是完全闲置的没有做什么事情。

"""


import asyncio

async def display(num): # 异步函数
    await asyncio.sleep(1)
    print(num)

coroutines = [display(num) for num in range(10)] # 列表生成式

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(coroutines))
loop.close()

"""
执行上面的代码会发现，10个分别会阻塞1秒钟的协程总共只阻塞了约1秒种的时间，
这就说明协程对象一旦阻塞会将CPU让出而不是让CPU处于闲置状态，这样就大大的提升了CPU的利用率。
而且我们还会注意到，0到9的数字并不是按照我们创建协程对象的顺序打印出来的，这正是我
另外，多次执行该程序会发现每次输出的结果都不太一样，
这正是并发程序本身执行顺序不确定性造成的结果。

"""