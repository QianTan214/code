import matplotlib.pyplot as plt

def graph(x,y):
    print(f"function that graphs {x} and {y}")
    plt.plot(x,y)
    plt.show()


x = [1,2,3]
y = [3,2,1]

graph(x, y)