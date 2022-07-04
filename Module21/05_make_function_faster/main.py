def factorial(num, res=1):
    if num == 1:
        return res
    res *= num
    return factorial(num-1, res)


def calculating_math_func(data):
    result = factorial(data)
    result /= data ** 3
    result = result ** 10
    return result


