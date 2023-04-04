def factorial(n):
    if (n > 1):
        value = n * factorial(n - 1)
        print(str(n) + '! =' + str(value))
    else:
        value = 1
        print(str(n) + '! =' + str(value))
    return value


factorial(4)
