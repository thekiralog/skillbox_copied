while True:
    pas = input('Введите пароль: ')
    capitals = 0
    digits = 0
    for sym in pas:
        if sym.isupper():
            capitals += 1
        elif sym.isdigit():
            digits += 1
    if not len(pas) >= 8:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    elif not capitals > 0:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    elif not digits >= 3:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break
