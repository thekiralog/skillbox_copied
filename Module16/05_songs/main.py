violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

user_quantity = int(input('Сколько песен выбрать? '))
i = 1
ttl = 0
while i != user_quantity + 1:
    cheat_line = str('Название ') + str(i) + str(' песни: ')
    user_song = input(cheat_line)
    for key, value in violator_songs:
        if key == user_song:
            ttl += value
    i += 1
print('\n Общее время звучания песен:', round(ttl, 3), "минут")
