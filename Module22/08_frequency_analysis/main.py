def freq_sorting(data):
    sum_chars = sum(data.values())
    presorted_data = dict()
    for i_key, i_value in data.items():
        i_value = round(i_value / sum_chars, 3)
        if i_value in presorted_data.keys():
            presorted_data[i_value].append(i_key)
        else:
            presorted_data[i_value] = list(i_key)
    sorted_sheet = list()
    for i_key, i_value in sorted(presorted_data.items(), reverse=True):
        for j_elem in sorted(i_value):
            sorted_sheet.append((j_elem, i_key))
    return sorted_sheet


text = open('text.txt', 'r', encoding='utf-8')
analysis = open('analysis.txt', 'w', encoding='utf-8')

text_data = dict()
for i_string in text:
    for i_char in i_string.lower():
        if i_char.isalnum() and i_char != ' ':
            if i_char in text_data.keys():
                text_data[i_char] += 1
            else:
                text_data[i_char] = 1

sorted_data = freq_sorting(text_data)
for i_res in sorted_data:
    analysis.write(i_res[0] + ": " + str(i_res[1]) + '\n')
analysis.close()
text.close()

# зачтено
