import random

max_range = int(input('Введите максимальное число: '))
yup = set()
nah = set()
desired = str(random.randint(1, max_range))
print(desired)
while True:
    current_set = set()
    boris_guess = input('Нужное число есть среди вот этих чисел: ')
    if boris_guess == 'Помогите!':
        fancy_string = str()
        for i_num in yup:
            fancy_string = fancy_string + i_num + ' '
        print('Артём мог загадать следующие числа:', fancy_string[:-1])
        break
    else:
        boris_guess.split()
        for i_num in boris_guess:
            if i_num.isnumeric():
                current_set.add(i_num)
    if desired in current_set:
        print('Да')
        yup.update(current_set)
    else:
        print('Нет')
        nah.update(current_set)
    yup.difference_update(nah)
