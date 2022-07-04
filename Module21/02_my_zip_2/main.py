def min_len(obj_1, obj_2):
    return range(min(len(obj_1), len(obj_2)))


def my_zip(iter_1, iter_2):  # Искренне не понимаю, как улучшить имеющийся код
    iter_1 = list(iter_1)
    iter_2 = list(iter_2)
    result = ((iter_1[i_elem], iter_2[i_elem])
              for i_elem in min_len(iter_1, iter_2))
    return result


print(my_zip('fsagsa', {10, 5, 6}))
for i in my_zip('fsagsa', {10, 5, 6}):
    print(i)
