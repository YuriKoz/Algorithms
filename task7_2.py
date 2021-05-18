from random import randint

array = [randint(-100, 100) for _ in range(10)]


def merge_sort(nums):
    if len(nums) > 1:
        center = len(nums) // 2
        left = nums[:center]
        right = nums[center:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        return nums


print('Исходный массив:', array)
print('Сортировка слиянием:', merge_sort(array[:]))
