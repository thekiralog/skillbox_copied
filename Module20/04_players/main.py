players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

whole_data_players = list()
for i_key, i_value in players.items():
    player = list()
    for name in i_key:
        player.append(name)
    for score in i_value:
        player.append(score)
    player = tuple(player)
    whole_data_players.append(player)
print(whole_data_players)
