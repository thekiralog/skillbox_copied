import random


def tpl_sort(mass):
    mass = sorted(list(mass_to_sort))
    mass = tuple(mass)  # В этом суть задания, или нужно было реализовать алгоритм сортировки, например пузырьковую?
    return mass


mass_to_sort = tuple([random.randint(-99, 99) for _ in range(10)])
print(mass_to_sort)
print(tpl_sort(mass_to_sort))

