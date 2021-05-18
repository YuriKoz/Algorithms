array = [2, 8, 5, 1, 4]
# array = [-5, 11, 4, 22, 53, 12, -76]


def median(nums):
    half = len(nums) // 2
    nums.sort()
    if not len(nums) % 2:
        return (nums[half - 1] + nums[half]) / 2
    return nums[half]


print('Исходный массив:', array)
print('Медиана:', median(array[:]))
