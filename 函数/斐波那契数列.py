def fibonacci(n):
    f0 = 0
    f1 = 1
    while f0 < n:
        print(str(f0) + '')
        temp = f1
        f1 = f0 + f1
        f0 = temp
    print()


fibonacci(100)
