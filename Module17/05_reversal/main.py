def reversed_split(text, char) -> str:
    text = text.split(char, 1)
    text = text[1].rsplit(char, 1)
    text = text[0]
    return text[::-1]


user_text = input('Введите строку: ')
user_char = input('Введите граничный символ: ')
print('Развернутая последовательность между первым и последним', user_char, '-', reversed_split(user_text, user_char))
