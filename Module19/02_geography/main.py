cntry_quantity = int(input('Количество стран: '))
num_to_str = ['Первая', 'Вторая', 'Третья', 'Четвёртая', 'Пятая', 'Шестая', 'Седьмая', 'Восьмая', 'Девятая']
cities_str = ['первый', 'второй', 'третий']
cntry_data = dict()
for cntry_num in range(0, cntry_quantity):
    cntry_cities = input(f'{num_to_str[cntry_num]} страна: ').split()
    cntry_data[cntry_cities[0]] = cntry_cities[1::]
for iteration in range(0, 3):
    city = input(f'Введите {cities_str[iteration]} город: ')
    for key, value in cntry_data.items():
        if value.count(city) > 0:
            print(f'Город {city} расположен в стране {key}')
        else:
            print(f'По городу {city} нет данных')
            break
