import random


def least_divisor(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return i
    return n


dividend = random.randint(2, 9999)

print(dividend, least_divisor(dividend))

