user_text = input('Введите текст: ')
vowels = set('аиоуеэюёыя')
user_vowels = list()
for char in user_text:
    if char in vowels:
        user_vowels.append(char)
print('Список гласных букв:', user_vowels)
print('Длина списка:', len(user_vowels))
