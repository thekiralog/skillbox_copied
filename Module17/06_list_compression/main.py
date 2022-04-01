import random

nums_quantity = int(input('Количество чисел в строке: '))
nums = [random.randint(0, 2) for num in range(nums_quantity)]
print('Список до сжатия:', nums)
i = 0
for index, i_num in enumerate(nums):
    if i_num > min(nums):
        nums.insert(i, nums.pop(index))
        i += 1
nums = nums[0:nums.index(min(nums))]
print('Список после сжатия:', nums)
