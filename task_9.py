num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите второе число: '))

if num_2 < num_1 < num_3 or num_3 < num_1 < num_2:
    print(f'Среднее число: {num_1}')
elif num_1 < num_2 < num_3 or num_3 < num_2 < num_1:
    print(f'Среднее число: {num_2}')
else:
    print(f'Среднее число: {num_3}')
