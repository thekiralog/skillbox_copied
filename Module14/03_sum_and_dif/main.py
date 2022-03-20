def sum_n_dif(n: int):
    total = 0
    for i in str(n):
        total += int(i)

        def len_of_n(n: int):
            length = len(str(n))
            return length

    dif = total - len_of_n(n)
    return print('\nСумма цифр:', total,
                 '\nКоличество цифр в числе:', len_of_n(n),
                 '\nРазность суммы и количества цифр:', dif)


def sum_n_dif_2(n: int):
    total = 0
    for i in str(n):
        total += int(i)
    return print('\nСумма цифр:', total,
                 '\nКоличество цифр в числе:', len(str(n)),
                 '\nРазность суммы и количества цифр:', total - len(str(n)))


# sum_n_dif(int(input('Введите число:')))
sum_n_dif_2(int(input('Введите число:')))


