import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

num = array[0]
num_of_rep = 1
for i in range(SIZE - 1):
    rep = 1
    for j in range(i + 1, SIZE):
        if array[i] == array[j]:
            rep += 1
    if rep > num_of_rep:
        num_of_rep = rep
        num = array[i]

if num_of_rep > 1:
    print(f'{num_of_rep} раз(а) встречается число {num}')
else:
    print('Все элементы уникальны')
