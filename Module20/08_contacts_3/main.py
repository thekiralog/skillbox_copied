data = dict()
while True:
    if len(data) > 0:
        print('Текущий список контактов:', data)
    action = int(
        input(
            'Введите номер действия:\n'
            '1. Добавить контакт\n'
            '2. Найти человека\n')
    )
    if action == 1:
        name = tuple(input('Введите имя и фамилию человека: ').split())
        phone_num = input('Введите номер телефона: ')
        if name not in data:
            data[name] = phone_num
        else:
            print('Этот человек уже есть в контактах!')
            continue
    if action == 2:
        req_surname = input('Введите фамилию: ')
        if req_surname[-1] == 'а':
            req_surname = req_surname[:-1]
        for name in data.keys():
            if req_surname in name or req_surname + 'а' in name:
                print(name[0], name[1], data[name])
            else:
                print('Такого человека нет в базе!')
