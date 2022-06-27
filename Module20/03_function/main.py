def slicer(something, key):
    flag = 0
    fst_item = None
    scd_item = None
    for index, i_value in enumerate(something):
        if i_value == key and flag == 0:
            flag += 1
            fst_item = index
        elif i_value == key and flag == 1:
            scd_item = index
            return something[fst_item:scd_item + 1]
    return something[fst_item:]


desired = tuple(input('Введите что нибудь: '))
slice_key = input('Ключевой элемент: ')
to_print_string = str()
for item in slicer(desired, slice_key):
    to_print_string += item
print(to_print_string)
