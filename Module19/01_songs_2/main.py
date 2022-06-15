violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

int_to_str = ['первой', 'второй', 'третьей', 'четвертой', 'пятой', 'шестой', 'седьмой', 'восьмой', 'девятой']
while True:
    user_number = int(input('Сколько песен выбрать, до девяти: ')) - 1
    if 0 < user_number < 10:
        break
    else:
        print('Введите корректное значение, от 1 до 9.')
ttl_length = int()
for num in range(0, user_number + 1):
    while True:
        user_song = input(f'Введите название {int_to_str[num]} песни: ')
        if user_song in violator_songs:
            ttl_length += violator_songs[user_song]
            break
        else:
            print('В списке нет такой песни.')
print('\nОбщая длительность песен:', round(ttl_length, 2))
