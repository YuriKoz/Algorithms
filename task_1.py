u_num = int(input('Введите трехзначное число: '))
f_num = u_num // 100
s_num = u_num // 10 % 10
t_num = u_num % 10
summ = f_num + s_num + t_num
mult = f_num * s_num * t_num
print(f'Сумма = {summ}')
print(f'Произведение = {mult}')
