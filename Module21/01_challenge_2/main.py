def from_1_to_num(num):
    if num != 1:
        from_1_to_num(num - 1)
    return print(num)


user_num = int(input('Введите число: '))
from_1_to_num(user_num)
