def flatter(obj: list, result=list()):
    for item in obj:
        if isinstance(item, int):
            result.append(item)
        else:
            flatter(item, result)
    return result


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

better_list = flatter(nice_list)
print(better_list)
