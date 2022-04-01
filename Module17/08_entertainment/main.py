import random

sticks_quantity = int(input('Количество палок: '))
sticks = ['I' for stick in range(0, sticks_quantity)]
throws_quantity = int(input('Количество бросков: '))
downed_sticks = list()
i = 1
while i != throws_quantity + 1:
    left_stick = random.randint(1, sticks_quantity)
    right_stick = random.randint(left_stick, sticks_quantity)
    downed_sticks += [stick for stick in range(left_stick, right_stick + 1)]
    print('Бросок', str(i) + str('.'), 'Сбиты палки с номера', str(left_stick), 'по номер', right_stick)
    i += 1
downed_sticks = set(downed_sticks)
for index in downed_sticks:
    sticks[index - 1] = '.'
res = ''
for stick in sticks:
    res += stick + ' '
print('\nРезультат:', res)

