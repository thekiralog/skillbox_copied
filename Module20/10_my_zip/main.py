def my_zip(iter_1, iter_2):
    result = ((iter_1[i_elem], iter_2[i_elem])
              for i_elem in range(min(len(iter_1), len(iter_2))))
    return result


user_str = input('Строка: ')
user_tpl = tuple(input('Кортеж чисел (через пробел): ').split())
print(my_zip(user_str, user_tpl))
for i_item in my_zip(user_str, user_tpl):
    print(i_item)
