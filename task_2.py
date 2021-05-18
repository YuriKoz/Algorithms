num_1 = 5
num_2 = 6

and_op = num_1 & num_2
xor_op = num_1 ^ num_2
or_op = num_1 | num_2
inv_1 = ~num_1
inv_2 = ~num_2
r_shift = num_1 >> 2  # 5 // (2 * 2)
l_shift = num_1 << 2  # 5 * 2 * 2

print(and_op)
print(xor_op)
print(or_op)
print(inv_1)
print(inv_2)
print(r_shift)
print(l_shift)

# битовый сдвиг числа вправо равносилен целочисленному делению
# на 2 * n, где n количество знаков
# битовый сдвиг числа влево равносилен умножению
# на 2 * n, где n количество знаков
