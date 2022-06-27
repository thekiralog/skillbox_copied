import random

rnd_lst = [random.randint(0, 9) for _ in range(10)]
pairs = list()
for index, i_num in enumerate(rnd_lst):
    if index % 2 != 0:
        pairs.append((rnd_lst[index-1], rnd_lst[index]))

print(rnd_lst)
print(pairs)
