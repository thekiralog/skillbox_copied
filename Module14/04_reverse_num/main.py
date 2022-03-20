fst_num = input('Введите первое число:')
scd_num = input('Введите второе число:')
fst_num = fst_num.split('.')
scd_num = scd_num.split('.')
for i in range(2):
    fst_num[i] = fst_num[i][::-1]
    scd_num[i] = scd_num[i][::-1]
fst_num.insert(1, '.')
scd_num.insert(1, '.')
rev_fst_num = ''
rev_scd_num = ''
for i in range(3):
    rev_fst_num += fst_num[i]
    rev_scd_num += scd_num[i]

print('\nПервое число наоборот:', rev_fst_num,
      '\nВторое число наоборот:', rev_scd_num,
      '\nСумма:', float(rev_fst_num) + float(rev_scd_num))
