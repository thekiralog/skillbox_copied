text = input('Введите текст для анализа: ')
hist = dict()
for i_sym in text:
    if i_sym in hist:
        hist[i_sym] += 1
    else:
        hist[i_sym] = 1
inverted_hist = dict()
for key, value in hist.items():
    if value in inverted_hist:
        inverted_hist[value].append(key)
    else:
        inverted_hist[value] = list(key)
for key in sorted(inverted_hist.keys()):
    print(f'{key} : {inverted_hist[key]}')
