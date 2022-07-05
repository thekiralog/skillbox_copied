def value_changer(data=None, key_1='title', key_2='h2', new_value=None):
    if key_1 in data:
        data[key_1] = f'Куплю/продам {new_value} недорого'
    if key_2 in data:
        data[key_2] = f'У нас самая низкая цена на {new_value}'
    for item in data.values():
        if isinstance(item, dict):
            value_changer(item, key_1, key_2, new_value)
    return data


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

site_quantity = int(input('Сколько сайтов: '))
for action in range(site_quantity):
    phone_vendor = input('Введите название продукта для нового сайта: ')
    print('Сайт для', phone_vendor)
    print(value_changer(data=site, new_value=phone_vendor))
