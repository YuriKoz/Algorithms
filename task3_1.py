# Первый вариант
array = [0] * 8
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            array[j - 2] += 1
i = 0
print()

while i < len(array):
    print(f'Числу {i + 2} кратны {array[i]} чисел(а)')
    i += 1
print()

# Второй вариант
result = {}
for i in range(2, 10):
    result[i] = []
    for j in range(2, 100):
        if j % i == 0:
            result[i].append(j)
    print(f'Для числа {i} кратны - {len(result[i])} чисел(а)')
