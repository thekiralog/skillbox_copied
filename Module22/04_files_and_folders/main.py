import os


def catalog_content(current_path, content=[]):
    for i_elem in os.listdir(current_path):
        path = os.path.join(current_path, i_elem)
        if os.path.isfile(path):
            content.append(path)
        if os.path.isdir(path):
            content.append(path)
            catalog_content(path, content)
    return content


user_path = "../../Module14"
common_file_size = 0
sub_folders_quantity = 0
files_quantity = 0

for i_path in catalog_content(user_path):
    if os.path.isfile(i_path):
        common_file_size += os.path.getsize(i_path)
        files_quantity += 1
    elif os.path.isdir(i_path):
        sub_folders_quantity += 1

print(
    '{input_path}\n'
    'Размер каталога (в Кб): {common_size}\n'
    'Количество подкаталогов: {sub_folders}\n'
    'Количество файлов: {files_quantity}'.format(
        input_path=user_path,
        common_size=common_file_size / 1024,
        sub_folders=sub_folders_quantity,
        files_quantity=files_quantity
    )
)

# зачтено
