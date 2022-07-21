def fib(num: int):
    if num in (1, 2):
        return 1
    return fib(num - 1) + fib(num - 2)


print(fib(10))
