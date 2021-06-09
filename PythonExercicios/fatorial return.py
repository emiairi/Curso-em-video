def fatorial(num=1):
    f = 1
    for i in range(num, 0, -1):
        f *= i
    return f


f1 = fatorial(5)
print(f1)