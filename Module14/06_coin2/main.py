print('Введите координаты монетки:')
coin_x = float(input('X:'))
coin_y = float(input('Y:'))
radius = float(input('Введите радиус:'))

if ((coin_x * coin_x) + (coin_y * coin_y)) ** 2 <= radius * radius:
    print('Монетка где-то рядом!')
else:
    print('Монетки здесь нет.')
