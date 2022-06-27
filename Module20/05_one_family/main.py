community_data = {
    1: {
        'name': 'Алена',
        'surname': 'Яшина',
        'age': 23,
    },
    2: {
        'name': 'Пётр',
        'surname': 'Яшин',
        'age': 24,
    },
    3: {
        'name': 'Василий',
        'surname': 'Яшин',
        'age': 22,
    },
    4: {
        'name': 'Артём',
        'surname': 'Чуйкин',
        'age': 28,
    },
    5: {
        'name': 'Слава',
        'surname': 'Потанин',
        'age': 25,
    },
    6: {
        'name': 'Лера',
        'surname': 'Потанина',
        'age': 23,
    },
    7: {
        'name': 'Гоша',
        'surname': 'Потнин',
        'age': 19,
    }
}

req_surname = input('Введите фамилию: ')
if req_surname[-1] == 'а':
    req_surname = req_surname[:-1]

for i_id, i_value in community_data.items():
    for surname in i_value.values():
        if req_surname == surname or req_surname + 'а' == surname:
            print(f'{surname} {i_value["name"]} {i_value["age"]}\n'
                  f'id человека в базе {i_id}')



