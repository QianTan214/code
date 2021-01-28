# lambda表达式用来排序，可用于数据处理中

countries = []

with open("country.csv", "r") as file:
    for line in file:
        line = line.strip() # 删除前后空格
        arr = line.split(";")
        name = arr[1]
        capital = arr[3]
        population = int(arr[4])
        countries.append((name, capital, population))

"""
# 定义一个函数排序
def get_population(country):
    return country[2]
countries.sort(key = get_population, reverse = True)
"""


# 用lambda函数排序
countries.sort(key = lambda x: -x[2]) # 根据人口从大到小排序


for country in countries[:3]:
    print(country)




# lambda表达式用在复合函数里

def quadratic(a, b, c):
    return lambda x: a*x*x + b*x + c

print(quadratic(1,-1, 2)(5)) # 这种写法
