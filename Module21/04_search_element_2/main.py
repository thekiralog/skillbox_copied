def key_finder(data, key):
    if key in data:
        return data[key]
    for item in data.values():
        if isinstance(item, dict):
            result = key_finder(item, key)
            if result:
                break
    else:
        result = None
    return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

user_key = input('Введите ключ, значение которого нужно найти: ')
user_answer = input('Хотите ввести максимальную глубину? Y/N: ').upper()
if user_answer == 'Y':
    user_depth = int(input('Введите максимальную глубину: '))
if key_finder(site, user_key) is None:
    print('Такого ключа нет в структуре')
else:
    print(key_finder(site, user_key))
