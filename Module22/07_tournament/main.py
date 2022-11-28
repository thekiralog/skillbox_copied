first_tour = open('first_tour.txt', 'r', encoding='utf-8')
second_tour = open('second_tour.txt', 'w', encoding='utf-8')

competition_members = dict()
score_to_approve = 0

for i_string in first_tour:
    if i_string[-1:] == '\n':
        i_string = i_string[0:-1]
        if i_string.isnumeric():
            score_to_approve = int(i_string)
        else:
            i_string = i_string.split()
            if int(i_string[2]) > score_to_approve:
                form = i_string[1][0] + '. ' + i_string[0]
                competition_members[form] = int(i_string[2])

second_tour.write(str(len(competition_members.items())) + '\n')
player_place = 1
for i_player in sorted(competition_members.items())[::-1]:
    form = str(player_place) + ') ' + i_player[0] + ' ' + str(i_player[1]) + '\n'
    player_place += 1
    second_tour.write(form)

first_tour.close()
second_tour.close()

# зачтено
