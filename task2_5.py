for el in range(32, 128):
    if el == 32:
        print(f'{el} - "{chr(el)}" - Это пробел')
    else:
        print(f'{el} - "{chr(el)}"')
    if el % 10 == 0:
        print()
