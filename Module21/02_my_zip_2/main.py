def min_len(obj_1, obj_2):
    return range(min(len(obj_1), len(obj_2)))


def my_zip(iter_1, iter_2):
    result = ((iter_1[i_elem], iter_2[i_elem])
              for i_elem in min_len(iter_1, iter_2))
    return result


user_str = input('Строка: ')
user_tpl = tuple(input('Кортеж чисел (через пробел): ').split())
print(my_zip(user_str, user_tpl))

