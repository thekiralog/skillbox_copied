N = int(input('Введите длину списка: '))
res = [(1 if x % 2 == 0
        else x % 5) for x in range(N)]
print(res)
