import os
import string


def is_file_exist(path):
    if os.path.exists(path):
        return True
    else:
        return False


user_string = input('Введите строку: ')
local_disks = list()
for i_letter in string.ascii_uppercase:
    i_disk = i_letter + ':\\'
    if os.path.isdir(i_disk):
        local_disks.append(i_disk)
print('Введите номер диска на котором хотите сохранить файл:', str(local_disks)[1:-1])
user_disk = local_disks[int(input())-1]
user_path = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел):').split()
file_path = str()
for i_folder in user_path:
    file_path += i_folder + '\\'
file_path = os.path.join(user_disk, file_path)
file_name = input('Введите имя файла: ') + '.txt'
file_path = os.path.join(file_path, file_name)
file = open(file_path, 'w', encoding='utf-8')
if is_file_exist(file_path):
    user_rewrite = input('Вы действительно хотите перезаписать файл? ').lower()
    if user_rewrite == 'да':
        print('Файл успешно перезаписан!')
        file.write(user_string)
    else:
        exit()
else:
    print('Файл успешно сохранен!')
    file.write(user_string)
file.close()
