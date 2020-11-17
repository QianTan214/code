

# KeyError异常
bag = ['apple', 'orange', 'cherry', 'apple','apple', 'cherry', 'blueberry']
count = {}
for fruit in bag:
    count[fruit] += 1

错误：
KeyError: 'apple'



# defaultdict类避免KeyError异常:

import collections
bag = ['apple', 'orange', 'cherry', 'apple','apple', 'cherry', 'blueberry']
count = collections.defaultdict(int)
for fruit in bag:
    count[fruit] += 1

输出：
defaultdict(<class 'int'>, {'apple': 3, 'orange': 1, 'cherry': 2, 'blueberry': 1})