guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    leave_or_come = input('Гость пришел или ушел? ')
    if leave_or_come == 'пора спать':
        print('Party is over, all folks are sleeping now.')
        break
    guest_name = input()
    if len(guests) < 6 and leave_or_come == 'пришел':
        guests.append(guest_name)
        print('Имя гостя:', guest_name,
              '\nПривет,', guest_name, '!')
    elif leave_or_come == 'ушел':
        if guests.count(guest_name) > 0:
            guests.remove(guest_name)
            print('Имя гостя:', guest_name,
                  '\nПока,', guest_name, '!')
        else:
            print('А ведь такого гостя нет..')
    else:
        print('Прости,', guest_name, 'но мест нет.')
