user_ip = input('Введите IP: ').split('.')
correct_block = 0
for block in user_ip:
    if len(user_ip) != 4:
        print('Адрес — это четыре числа, разделённые точками.')
        break
    elif not block.isdigit():
        print(f'{block} - это не целое число.')
        break
    elif int(block) > 255:
        print(f'{block} превышает 255.')
        break
    else:
        correct_block += 1
if correct_block == 4:
    print('IP-адрес корректен!')
