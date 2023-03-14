<<<<<<< HEAD
# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('введите число x: '))
y = int(input('введите число y: '))
z = int(input('введите число z: '))
if not(x or y or z) == (not x and not y and not z):
    print('истина')
else:
    print('ложь')


# def inputNumbers(x):
#     xyz = ["X", "Y", "Z"]
#     a = []
#     for i in range(x):
#         a.append(input(f"Введите значение {xyz[i]}: "))
#     return a
#
#
# def checkPredicate(x):
#     left = not (x[0] or x[1] or x[2])
#     right = not x[0] and not x[1] and not x[2]
#     result = left == right
#     return result
#
#
# statement = inputNumbers(3)
#
# if checkPredicate(statement) == True:
#     print(f"Утверждение истинно")
# else:
#     print(f"Утверждение ложно")
=======
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from math import factorial

number = int(input('Введите число '))

print(f'Произведение введённого числа {list(map(lambda x: ((x == 1) and 1) or x * factorial(x - 1), list(range(1, number+1))))}')
>>>>>>> e77508f5901b74bbea075419ce6277b9f23b9102
