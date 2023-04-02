def factorial(n):
    i = 1
    f = 1
    while i < n + 1:
        f = f * i
        i += 1
    return f


print('3!=' + str(factorial(3)))
