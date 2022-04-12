fst_str = list(input('Введите первую строку: '))
scd_str = list(input('Введите вторую строку: '))
shift = 0
if len(fst_str) == len(scd_str):
    for i_sym in fst_str:
        if fst_str.count(i_sym) != scd_str.count(i_sym):
            print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
    for _ in range(len(fst_str)):
        if fst_str == scd_str:
            print(f'Первая строка получается из второй со сдвигом {shift}')
            break
        else:
            shift += 1
            fst_str.append(fst_str.pop(0))
if fst_str != scd_str:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
