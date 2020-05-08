# 99乘法表
def multiplication_table():
    for i in range(1, 10):
        for j in range(1, 10):
            print(j, "x", i, "=", i * j, "\t", end="")
            if i == j:
                print("")
                break


# 斐波那契数列 从0，1开始，第三项为前两项之和
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


# multiplication_table()

print(fib(12))
