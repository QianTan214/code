a = [1,2,3,4,5,6]

# for i in a:
#     print(i)

# it = iter(a)
it = a.__iter__()
print(it)

while True:
    try:
        # val = it.__next__()
        val = next(it) # next 函数取iter里下一个值
    except StopIteration:
        break
    print(f'{val=}')
