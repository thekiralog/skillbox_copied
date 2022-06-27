gamers_data = dict()
games_qnt = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя):')
for game in range(1, games_qnt + 1):
    game_res = input(f'{game}-я запись: ').split()
    game_res[0] = int(game_res[0])
    if game_res[1] not in gamers_data:
        max_score_index = game + 1
        max_score = game_res[0]
        max_ttl = (max_score, max_score_index)
        gamers_data[game_res[1]] = max_ttl
    else:
        if game_res[0] > max_score:
            max_score = game_res[0]
            max_score_index = game
            del(gamers_data[game_res[1]])
            del(max_ttl)
            max_ttl = (max_score, max_score_index)
            gamers_data[game_res[1]] = max_ttl
        continue
print(gamers_data)
for gamer in gamers_data.values():
    for score in gamer:
        pass
