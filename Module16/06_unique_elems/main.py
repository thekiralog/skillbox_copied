i = 0
fst_list = list()
scd_list = list()
while i != 3:
    cheat = str('Введите ') + str(i + 1) + str(' число для первого списка: ')
    fst_list.append(int(input(cheat)))
    i += 1
i = 0
while i != 7:
    cheat = str('Введите ') + str(i + 1) + str(' число для второго списка: ')
    scd_list.append(int(input(cheat)))
    i += 1
i = 0
unique_list = set(fst_list + scd_list)
print('\nПервый список:', fst_list,
      '\nВторой список:', scd_list,
      '\n\nНовый список с уникальными элементами:', sorted(list(unique_list)))
