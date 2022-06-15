def keys_dict(dom, counter: int, res: dict):
    if isinstance(dom, dict):
        for key, value in dom.items():
            res[key] = counter
            if isinstance(value, list):
                counter += 1
                for i_dict in value:
                    keys_dict(i_dict, counter, res)
    return res


def finder(dom, desired, new_kid):
    if isinstance(dom, dict):
        for key, value in dom.items():
            if desired == key:
                upd = {legacy[0]: []}
                dom[key].append(upd)
            elif isinstance(value, list):
                for i_dict in value:
                    finder(i_dict, desired, new_kid)
    return


int_to_str = ['Первая', 'Вторая', 'Третья', 'Четвёртая', 'Пятая', 'Шестая', 'Седьмая', 'Восьмая', 'Девятая']
pairs_quantity = int(input('Введите количество человек: '))
nesting = dict()
nesting_lvl = 0
legacy = input(f'{int_to_str[0]} пара: ').split()
pedigree = {legacy[1]: [{legacy[0]: []}]}
for _ in range(1, pairs_quantity):
    legacy = input(f'{int_to_str[_]} пара: ').split()
    child = legacy[0]
    parent = legacy[1]
    finder(pedigree, legacy[1], legacy[0])
keys_dict(pedigree, nesting_lvl, nesting)
print('\n"Высота" каждого члена семьи:')
for i_key, i_value in nesting.items():
    print(i_key, i_value)
