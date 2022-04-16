msg = input('Сообщение: ')
res = list()
i = 0
while i != len(msg):
    cache = list()
    if msg[i].isalpha():
        start_index = i
        while True:
            if i + 1 < len(msg) and msg[i+1].isalpha():
                i += 1
            else:
                cache.append(msg[i:start_index:-1] + msg[start_index])
                res.append(cache[0])
                break
    else:
        res.append(msg[i])
    i += 1
print(''.join(res))
