import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array, '\n')

array_index_even = []

for count, val in enumerate(array):
    if val % 2 == 0:
        print(f'Индекс: {count} | Число: {val}')
        array_index_even.append(count)

print(f'\nИндексы чётных элементов первого массива: {array_index_even}')
