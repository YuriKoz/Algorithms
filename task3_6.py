import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_id = 0
max_id = 0

for i in range(1, SIZE):
    if array[i] < array[min_id]:
        min_id = i
    elif array[i] > array[max_id]:
        max_id = i

print(f'Минимальное число = {array[min_id]}, максимальное число = {array[max_id]}')

if min_id > max_id:
    min_id, max_id = max_id, min_id
amount = 0

for i in range(min_id+1, max_id):
    amount += array[i]
print(f'Сумма = {amount}')
