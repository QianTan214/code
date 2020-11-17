"""题目36：如何使用random模块生成随机数、实现随机乱序和随机抽样？"""

点评：送人头的题目，因为Python标准库中的常用模块应该是Python开发者都比较熟悉的内容，
这个问题回如果答不上来，整个面试基本也就砸锅了。

random.random()函数可以生成[0.0, 1.0)之间的随机浮点数。
random.uniform(a, b)函数可以生成[a, b]或[b, a]之间的随机浮点数。
random.randint(a, b)函数可以生成[a, b]或[b, a]之间的随机整数。
random.shuffle(x)函数可以实现对序列x的原地随机乱序。
random.choice(seq)函数可以从非空序列中取出一个随机元素。
random.choices(population, weights=None, *, cum_weights=None, k=1)函数
可以从总体中随机抽取（有放回抽样）出容量为k的样本并返回样本的列表，
可以通过参数指定个体的权重，如果没有指定权重，个体被选中的概率均等。
random.sample(population, k)函数可以从总体中随机抽取（无放回抽样）
出容量为k的样本并返回样本的列表。

扩展：random模块提供的函数除了生成均匀分布的随机数外，还可以生成其他分布的随机数，
例如random.gauss(mu, sigma)函数可以生成高斯分布（正态分布）的随机数；
random.paretovariate(alpha)函数会生成帕累托分布的随机数；
random.gammavariate(alpha, beta)函数会生成伽马分布的随机数。