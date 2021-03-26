from cs50 import get_float



while True:

    change = get_float("Change owed: ")

    if change > 0:

        break


cents = change * 100


n = 0

# python中用地板除 // 舍去小数部分。如 5 // 2 结果是 2。 1.0 // 2 结果是 0

# 整数除法执行地板除，如果是浮点数除法则执行精确除法。1 / 2 结果 0.5

# 精确除法用 from __future__ import division。 如 1 / 2 结果 0.5

if cents % 25 >= 0 and cents % 25 < 25:
    n = n + cents // 25
    cents = cents - 25 * (cents // 25)

if cents % 10 >= 0 and cents % 10 < 10:
    n = n + cents // 10
    cents = cents - 10 * (cents // 10)


if cents % 5 >= 0 and cents % 5 < 5:
    n = n + cents // 5
    cents = cents - 5 * (cents // 5)

if cents < 5:
    n = n + cents // 1

print(f"{int(n)}")

