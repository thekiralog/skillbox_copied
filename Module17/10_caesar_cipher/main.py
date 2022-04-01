alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н",
            "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]

user_string = input('Введите текст: ')
shift = int(input('Введите сдвиг: '))
encode_alphabet = list(alphabet).copy()

for index in range(shift):
    encode_alphabet.append(encode_alphabet.pop(0))
result_string = str()
for char in user_string:
    if not char.isalpha():
        result_string += char
    elif char.isupper():
        char = encode_alphabet[alphabet.index(char.lower())]
        result_string += str.upper(char)
    else:
        char = encode_alphabet[alphabet.index(char)]
        result_string += char
print(result_string)
