<<<<<<< HEAD
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x_a = int(input('Введите координату Х точки А: '))
y_a = int(input('Введите координату Y точки А: '))
x_b = int(input('Введите координату X точки B: '))
y_b = int(input('Введите координату Y точки B: '))

distance = round(((x_b - x_a)**2 + (y_b - y_a)**2)**0.5, 2)
print(distance)
=======
# Реализуйте алгоритм перемешивания списка.

import random

def get_list(numbers, negative_range, positive_range):
    return [random.randint(negative_range, positive_range) for i in range(numbers)]


def shuffle_list(list1):
    return random.shuffle(list1)


numbers = 5 
negative_range = -10
positive_range = 10

sh_list = get_list(numbers, negative_range, positive_range)
print(sh_list)
shuffle_list(sh_list)
print(sh_list)
>>>>>>> e77508f5901b74bbea075419ce6277b9f23b9102
