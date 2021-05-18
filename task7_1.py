from random import randint

array = [randint(-100, 100) for _ in range(10)]


def bubble_reverse_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


print('Исходный массив:', array)
print('Обратная пузырьковая:', bubble_reverse_sort(array[:]))
