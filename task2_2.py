even = odd = 0
num = int(input('Введите натуральное число: \n'))
while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10
print(f'Четных цифр - {even} \nНечетных - {odd}')
