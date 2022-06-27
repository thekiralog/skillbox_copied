def my_zip(iter_1, iter_2):
    for action in range(min(len(iter_1), len(iter_2))):
        print((iter_1[action], iter_2[action]))


user_str = input('Строка: ')
user_tpl = tuple(input('Кортеж чисел (через пробел): ').split())
print(zip(user_str, user_tpl))
my_zip(user_str, user_tpl)
