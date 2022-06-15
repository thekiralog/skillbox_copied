def get_key(diction, desired):
    for key, value in diction.items():
        if value == desired:
            return key


low_synonyms = dict()
int_to_str = ['Первая', 'Вторая', 'Третья', 'Четвёртая', 'Пятая', 'Шестая', 'Седьмая', 'Восьмая', 'Девятая']
pairs_quantity = int(input('Введите количество пар слов: '))
for _ in range(0, pairs_quantity):
    string = input(f'{int_to_str[_]} пара: ').split('-')
    for index, item in enumerate(string):
        string[index] = item.strip()
    low_synonyms[string[0].lower()] = string[1].lower()
while True:
    user_word = input('Введите слово: ').lower()
    if user_word in low_synonyms.keys():
        print('Синоним:', low_synonyms[user_word])
        break
    elif user_word in low_synonyms.values():
        print('Синоним:', get_key(low_synonyms, user_word))
        break
    else:
        print('Такого слова в словаре нет.')


