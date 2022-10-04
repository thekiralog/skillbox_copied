import os

file = open('numbers.txt', 'r', encoding='utf-8')
answer = open('answer.txt', 'w', encoding='utf-8')
ans = 0
for i_elem in file.read():
    if i_elem.isnumeric():
        ans += int(i_elem)
print(ans)
answer.write(str(ans))
file.close()
answer.close()
