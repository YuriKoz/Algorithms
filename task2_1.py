while True:
    operation = input('Введите знак операции(+, -, *, /) или ноль для завершения: ')
    if operation == '0':
        print('Вы завершили работу калькулятора. Всего доброго.')
        break
    if operation == '+' or operation == '-' or operation == '*' or operation == '/':
        num_1 = int(input('Введите первое число: '))
        num_2 = int(input('Введите второе число: '))
        if operation == '+':
            print(f'Сумма = {num_1 + num_2}')
        elif operation == '-':
            print(f'Разность = {num_1 - num_2}')
        elif operation == '*':
            print(f'Произведение = {num_1 * num_2}')
        elif operation == '/':
            if num_2 != 0:
                print(f'Деление = {num_1 / num_2}')
            else:
                print('На ноль делить нельзя!')
    else:
        print('Неверная операция!')
