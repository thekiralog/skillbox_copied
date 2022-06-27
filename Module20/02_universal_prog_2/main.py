def is_prime(num):
    num = int(num)
    if num > 1:
        for i_num in range(2, num):
            if num % i_num == 0:
                return False
    else:
        return False
    return True


def even_items(built):
    res = list()
    if isinstance(built, dict):
        built = tuple(built.items())
    else:
        built = tuple(built)
    for index, value in enumerate(built):
        if is_prime(index):
            res.append(value)
    return res


some_string = 'Некий текст'
some_list = [1, 'takt', some_string, 161616]
some_tuple = ('prikol', 'ne_prikol', 'prikols', 151515, some_list, 'prikol')
some_dict = {'key_1': 'value_1', 'key_2': 'value_2))', 'key_3': 'value_3'}
some_set = {0, 1, 2, 3, 4, 5, 6, 7}
list_to_func = [some_string, some_list, some_tuple, some_dict, some_set]
for i_item in list_to_func:
    print(even_items(i_item))

