def get_key(dictionary, value, new_dict):
    for i_key, i_value in dictionary.items():
        if i_value == value:
            if i_key not in new_dict:
                new_dict[i_key] = i_value
            else:
                continue


top_gamers_data = dict()
games_qnt = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя):')
for game in range(1, games_qnt + 1):
    game_res = input(f'{game}-я запись: ').split()
    if game_res[1] not in top_gamers_data:
        max_score = game_res[0]
        top_gamers_data[game_res[1]] = int(game_res[0])
    else:
        if game_res[0] > max_score:
            del(top_gamers_data[game_res[1]])
            top_gamers_data[game_res[1]] = int(game_res[0])
print('Итоги соревнований:')
sorted_data = dict()
for i_score in sorted(top_gamers_data.values())[::-1]:
    get_key(top_gamers_data, i_score, sorted_data)
for name, score in sorted_data.items():
    print(f'{name}: {score}')


