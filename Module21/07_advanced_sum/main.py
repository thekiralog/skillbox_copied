def advanced_sum(*args, res=0):
    for arg in args:
        if isinstance(arg, int):
            res += arg
        else:
            for item in arg:
                res += advanced_sum(item)
    return res


print(advanced_sum([1, 2, [3, 4, [5]]]))


