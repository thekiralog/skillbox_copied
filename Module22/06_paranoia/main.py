alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cipher_alphabet = list.copy(alphabet)

cipher_alphabet.append(cipher_alphabet.pop(0))
origin_text = open('text.txt', 'r', encoding='utf-8')
cipher_text = open('cipher_text.txt', 'w', encoding='utf-8')

for i_string in origin_text:
    for i_elem in i_string:
        if i_elem.isupper():
            i_index = alphabet.index(i_elem.lower())
            cipher_text.write(cipher_alphabet[i_index].upper())
        elif i_elem.islower():
            i_index = alphabet.index(i_elem)
            cipher_text.write(cipher_alphabet[i_index])
        elif i_elem == '\n':
            cipher_alphabet.append(cipher_alphabet.pop(0))
            cipher_text.write('\n')
        else:
            cipher_text.write(i_elem)

origin_text.close()
cipher_text.close()

# зачтено
