import os

zen = open('zen.txt', 'r', encoding='utf-8')
zen_strings = list()
for i_elem in zen.read().split('\n'):
    zen_strings.append(i_elem)
for i_string in reversed(zen_strings):
    print(i_string)
zen.close()
