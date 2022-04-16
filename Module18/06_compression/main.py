user_str = input('Введите строку: ')
res = str()
counter = 1
for index, sym in enumerate(user_str):
    if index + 1 == len(user_str):
        res += str(sym) + str(counter)
        break
    elif user_str[index] == user_str[index + 1]:
        counter += 1
    else:
        res += str(sym) + str(counter)
        counter = 1
print(res)
