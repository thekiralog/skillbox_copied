count = 0
legs_size = list()
roller_size = list()
people_quantity = int(input('Кол-во людей:'))
while count != people_quantity:
    cheat = str('Размер ноги ') + str(count + 1) + str(' человека: ')
    legs_size.append(int(input(cheat)))
    count += 1
count = 0
shoes_quantity = int(input('Количество коньков:'))
while count != shoes_quantity:
    cheat = str('Размер ') + str(count + 1) + str(' пары: ')
    roller_size.append(int(input(cheat)))
    count += 1
count = 0
for n in legs_size:
    for k in roller_size:
        if k >= n:
            roller_size.remove(k)
            count += 1
            break
print('Наибольшее кол-во людей, которые могут взять ролики:', count)
