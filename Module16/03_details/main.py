shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

user_key = input()
ttl = 0
quantity = 0
for key, value in shop:
    if user_key == key:
        ttl += value
        quantity += 1
if quantity > 0:
    print('Название детали:', user_key,
          '\n\nКол-во деталей:', quantity,
          '\nОбщая стоимость:', ttl)
else:
    print('Такой детали нет!')
