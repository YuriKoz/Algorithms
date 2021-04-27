num = int(input('Введите натуральное число: \n'))
result = 0
while num > 0:
    result = result * 10 + num % 10
    num //= 10
print(f'Получилось число: {result}')
