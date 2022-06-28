def fib(pos_num, prev_num=1, cur_num=1, fib_lst=[]):
    while len(fib_lst) != pos_num:
        fib_lst.append(cur_num)
        fib_lst.append(prev_num)
        cur_num += prev_num
        prev_num += cur_num
        fib(pos_num, prev_num, cur_num)
    return fib_lst[-1]


print(fib(10))
