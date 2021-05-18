_n = 1


def first(_n):
    if _n == 1:
        return _n
    elif _n > 0:
        return _n + first(_n-1)


def second(_n):
    return _n * (_n + 1) // 2


while _n < 901:  # не будем переполнять стек, если же неважно, то while True
    if first(_n) == second(_n):
        print(f'Для n = {_n} - True')
    else:
        print(f'Для n = {_n} - False')
        break
    _n += 1
