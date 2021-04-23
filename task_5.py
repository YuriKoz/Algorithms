chr_1 = ord(input('Введите первую букву: '))
chr_2 = ord(input('Введите вторую букву: '))
chr_1 = chr_1 - ord('a') + 1
chr_2 = chr_2 - ord('a') + 1
distance = abs(chr_1 - chr_2) - 1
print(f'Первая буква на позиции {chr_1}, вторая на позиции {chr_2}')
print(f'Между буквами находится {distance} букв.')
