import random

fst_team = [round(float(random.randint(1, 100)
                        + random.randint(1, 100) / 100), 3) for _ in range(20)]
scd_team = [round(float(random.randint(1, 100)
                        + random.randint(1, 100) / 100), 3) for _ in range(20)]
winners = list()
for competitor in range(20):
    if fst_team[competitor] > scd_team[competitor]:
        winners.append(fst_team[competitor])
    else:
        winners.append(scd_team[competitor])

print('Первая команда:', fst_team)
print('Вторая команда:', scd_team)
print('Победители тура:', winners)
