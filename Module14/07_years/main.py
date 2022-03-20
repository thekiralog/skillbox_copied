fst_val = int(input('Введите первый год:'))
scd_val = int(input('Введите второй год:'))
correct_values = list()
for i in range(fst_val, scd_val):
    for elem in str(i):
        if str(i).count(elem) >= 3:
            correct_values.append(i)
            break
print('Года от', fst_val, 'до', scd_val, 'с тремя одинаковыми цифрами:')
for i in correct_values:
    print(i)
