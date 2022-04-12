text = input('Введите строку: ').split()
for word in text:
    if len(word) == len(max(text)):
        print(f'Самое длинное слово: {word}'
              f'\nДлина этого слова: {len(word)}')
        break
