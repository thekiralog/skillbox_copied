import random


def numeric_palindrome(desired: list,):
    for index, value in enumerate(desired[::-1]):
        if index > -1 or desired[value] != desired[index - 1]:
            index -= 1
            numeric_palindrome(desired[index::-1])
        elif index > -1 and desired[value] == desired[index - 1]:
            index -= 1
            numeric_palindrome(desired[index::-1])
        else:
            return len(desired[:index])


number = [random.randint(1, 9) for _ in range(random.randint(4, 5))]
print(number)
print(numeric_palindrome(number))
print(number[:numeric_palindrome(number)])




