text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt ' \
       'cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp ' \
       'djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst ' \
       'tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ' \
       'ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf' \
       ' wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh' \
       ' x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju' \
       ' znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
encode_alphabet = list(alphabet).copy()
encode_alphabet.insert(0, encode_alphabet.pop(len(encode_alphabet) - 1))
correct_chars_flatted = str()
for char in text:
    if not char.isalpha():
        correct_chars_flatted += char
    elif char.isupper():
        char = encode_alphabet[alphabet.index(char.lower())]
        correct_chars_flatted += str.upper(char)
    else:
        char = encode_alphabet[alphabet.index(char)]
        correct_chars_flatted += char
correct_chars_flatted = correct_chars_flatted.split()
prefixed_words = list()
for index, word in enumerate(correct_chars_flatted):
    prefixed_words.append(list())
    for sym in word:
        prefixed_words[index].append(sym)
key_shift = 3
res = str(' ')
for index, word in enumerate(prefixed_words):
    for _ in range(key_shift):
        prefixed_words[index].insert(0, prefixed_words[index].pop(len(prefixed_words[index]) - 1))
    for sym in word:
        if sym == '/':
            sym = '\n'
            key_shift += 1
        elif sym == "(":
            sym = "'"
        res += sym
    res += ' '
print(prefixed_words)
print(res)
