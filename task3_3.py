import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Изначальный массив: {array}\n')

mini = 0
maxi = 0

for i in range(SIZE):
    if array[i] < array[mini]:
        mini = i
    elif array[i] > array[maxi]:
        maxi = i

print(f'Минимальное число - {array[mini]} | Индекс - {mini}')
print(f'Максимальное число {array[maxi]} | Индекс - {maxi}\n')
_ = array[mini]
array[mini] = array[maxi]
array[maxi] = _

print(f'Массив после замены: {array}')
