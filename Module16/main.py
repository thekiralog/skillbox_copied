import random


def numeric_palindrome(desired: list, ):
    reverse_desired = desired[::-1]
    if desired == reverse_desired:
        return True
    else:
        return False


numbers = [random.randint(0, 9) for _ in range(random.randint(4, 10))]
answer = list()
for i_num in range(0, len(numbers)):
    if numeric_palindrome(numbers[i_num:]):
        answer = numbers[:i_num]
        break
answer.reverse()

print('Исходный список', numbers)
print('Нужно чисел для палиндрома', len(answer))
print('Эти числа:', answer)

