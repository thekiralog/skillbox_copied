ppl_quantity = int(input('Кол-во человек: '))
del_num = int(input('Порядок пули в барабане: '))
print('Значит выбывает каждый', del_num, 'человек')

counter = 1
players = [player for player in range(1, ppl_quantity + 1)]
print('\nТекущий круг людей:', players,
      '\nНачало счёта с номера:', counter)
players_cycle = list(players).copy()

while len(players) != 1:
    for index, loser in enumerate(players_cycle):
        if counter == del_num:
            print('Человек под номером:', loser, 'получает пулю..')
            counter = 1
            players.remove(loser)
            players_cycle = players_cycle[index + 1:] + players_cycle[:index]
            if len(players) != 1:
                print('\nТекущий круг людей:', players,
                      '\nНачало счёта с номера:', players_cycle[0])
            else:
                print('\nВыжил номер', players_cycle[0])
            break
        else:
            counter += 1
