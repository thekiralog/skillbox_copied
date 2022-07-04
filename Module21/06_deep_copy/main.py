def value_changer(data, key, new_value):
    if key in data:
        data[key] = data[key].replace('телефон', new_value)
        return data[key]
    for item in data.values():
        if isinstance(item, dict):
            result = value_changer(item, key, new_value)
            if result:
                break
    else:
        result = None
    return result


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

# site_quantity = int(input('Сколько сайтов: '))
# for action in range(site_quantity):
#     phone_vendor = input('Введите название продукта для нового сайта: ')
#     print(f'Сайт для {phone_vendor}')
print(value_changer(site, 'title'))
print(site)
