friends_quantity = int(input('Количество друзей: '))
debts_quantity = int(input('Долговых расписок: '))
friends = the_dict = {friend: 0 for friend in range(1, friends_quantity + 1)}
for i in range(debts_quantity):
    print('\n', i + 1, ' расписка')
    to_friend = int(input('Кому: '))
    from_friend = int(input('От кого: '))
    equity = int(input('Сколько: '))
    friends[to_friend] -= equity
    friends[from_friend] += equity
print('\nБаланс друзей:')
for key, value in friends.items():
    print(key, ':', value)
