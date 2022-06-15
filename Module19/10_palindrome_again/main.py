def is_it_palindrome(desired: str):
    if desired == desired[::-1]:
        return True
    else:
        return False


def shuffle(data: dict, unchanged_data: dict, length: int, ctrl=0):
    if ctrl == length:
        return print('Нельзя сделать палиндром')
    string_to_check = str()
    for i in range(0, length):
        cache_sym = data[ctrl]
        data[ctrl] = unchanged_data[i]
        data[i] = cache_sym
        for value in data.values():
            string_to_check += value
        if is_it_palindrome(string_to_check):
            return print('Можно сделать палиндром')
        string_to_check = str()
    ctrl += 1
    shuffle(data, unchanged_data, length, ctrl)


user_string = input('Введите строку: ')
index_data = dict()
for index, sym in enumerate(user_string):
    index_data[index] = sym

shuffle(index_data, index_data, len(user_string))
