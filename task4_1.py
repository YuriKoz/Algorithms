import timeit
import cProfile


# Первый вариант


def without_dict(n):
    array = [0] * 8
    for i in range(2, n):
        for j in range(2, 10):
            if i % j == 0:
                array[j - 2] += 1
    i = 0
    print()

    while i < len(array):
        print(f'Числу {i + 2} кратны {array[i]} чисел(а)')
        i += 1
    print()


# without_dict(99)

# print(timeit.timeit('without_dict(5)', number=100, globals=globals()))  # 0.015741800000000007
# print(timeit.timeit('without_dict(10)', number=100, globals=globals()))  # 0.009134200000000002
# print(timeit.timeit('without_dict(15)', number=100, globals=globals()))  # 0.0255277
# print(timeit.timeit('without_dict(20)', number=100, globals=globals()))  # 0.006678099999999999
# print(timeit.timeit('without_dict(25)', number=100, globals=globals()))  # 0.0233851

# cProfile.run('without_dict(99)')
'''
23 function calls in 0.009 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task4_1.py:6(without_dict)
        1    0.009    0.009    0.009    0.009 {built-in method builtins.exec}
        9    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       10    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
# cProfile.run('without_dict(50_000)')
'''
3 function calls in 0.035 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.035    0.035 <string>:1(<module>)
        1    0.035    0.035    0.035    0.035 task4_1.py:6(without_dict)
        1    0.000    0.000    0.035    0.035 {built-in method builtins.exec}
        9    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       10    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
# cProfile.run('without_dict(1_000_000)')
'''
23 function calls in 0.602 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.602    0.602 <string>:1(<module>)
        1    0.602    0.602    0.602    0.602 task4_1.py:6(without_dict)
        1    0.000    0.000    0.602    0.602 {built-in method builtins.exec}
        9    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       10    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

# Второй вариант


def with_dict(n):
    result = {}
    for i in range(2, 10):
        result[i] = []
        for j in range(2, n):
            if j % i == 0:
                result[i].append(j)
        print(f'Для числа {i} кратны - {len(result[i])} чисел(а)')


# with_dict(9)

# print(timeit.timeit('with_dict(9)', number=100, globals=globals()))  # 0.0196961
# print(timeit.timeit('with_dict(10)', number=100, globals=globals()))  # 0.018890399999999995
# print(timeit.timeit('with_dict(15)', number=100, globals=globals()))  # 0.036143
# print(timeit.timeit('with_dict(20)', number=100, globals=globals()))  # 0.009083899999999999
# print(timeit.timeit('with_dict(25)', number=100, globals=globals()))  # 0.0143275

# cProfile.run('with_dict(99)')
'''
196 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task4_1.py:77(with_dict)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        8    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        8    0.000    0.000    0.000    0.000 {built-in method builtins.print}
      176    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
# cProfile.run('with_dict(50_000)')
'''
91462 function calls in 0.041 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.041    0.041 <string>:1(<module>)
        1    0.033    0.033    0.040    0.040 task4_1.py:77(with_dict)
        1    0.000    0.000    0.041    0.041 {built-in method builtins.exec}
        8    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        8    0.000    0.000    0.000    0.000 {built-in method builtins.print}
    91442    0.007    0.000    0.007    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
# cProfile.run('with_dict(1_000_000)')
'''
1828983 function calls in 0.780 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.018    0.018    0.780    0.780 <string>:1(<module>)
        1    0.609    0.609    0.762    0.762 task4_1.py:77(with_dict)
        1    0.000    0.000    0.780    0.780 {built-in method builtins.exec}
        8    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        8    0.000    0.000    0.000    0.000 {built-in method builtins.print}
  1828963    0.153    0.000    0.153    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

print('Первый вариант решения быстрее второго.')
