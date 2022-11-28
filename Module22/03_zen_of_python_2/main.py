import os


def key_finder(dictionary, value):
    for i_key in dictionary:
        if zen_dict[i_key] == value:
            return i_key


zen = open(os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt')), 'r', encoding='utf-8')
zen_dict = dict()

for i_elem in zen.read().lower():
    if i_elem.isalpha():
        if i_elem in zen_dict:
            zen_dict[i_elem] += 1
        else:
            zen_dict[i_elem] = 1
    else:
        continue

zen.seek(0)
zen_words_quantity = len(zen.read().split())
zen.seek(0)
zen_strings_quantity = len(zen.read().split('\n'))
key_with_lesser_value = key_finder(zen_dict, min(zen_dict.values()))
letters_sum = sum(zen_dict.values())

print(
    'Количество букв в файле: {letters}\n'
    'Количество слов в файле: {words}\n'
    'Количество строк в файле: {strings}\n'
    'Наиболее редкая буква: {most_rare}'.format(
        letters=letters_sum,
        words=zen_words_quantity,
        strings=zen_strings_quantity,
        most_rare=key_with_lesser_value
    )
)
zen.close()

# зачтено
