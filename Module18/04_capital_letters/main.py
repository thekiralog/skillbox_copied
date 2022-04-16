text = input('Введите строку: ').split()
res = str()
for word in text:
    res += word.capitalize() + ' '
print(res[:-1])
