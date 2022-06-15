pizza_gate = dict()
int_to_str = ['Первый', 'Второй', 'Третий', 'Четвёртый', 'Пятый', 'Шестой', 'Седьмой', 'Восьмой', 'Девятый']
orders_quantity = int(input('Введите количество заказов: '))
for _ in range(0, orders_quantity):
    order = input(f'{int_to_str[_]} заказ: ').split()
    order[2] = int(order[2])
    if order[0] not in pizza_gate:
        pizza_gate[order[0]] = {order[1]: order[2]}
    else:
        if order[1] not in pizza_gate[order[0]]:
            pizza_gate[order[0]][order[1]] = order[2]
        else:
            pizza_gate[order[0]][order[1]] += order[2]
print()
for key, value in pizza_gate.items():
    print(key, ':')
    for j_key, j_value in value.items():
        print('   ', j_key, ':', j_value)
