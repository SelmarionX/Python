<<<<<<< HEAD
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarternumber = int(input('введите номер четверти от 1 до 4: '))
if(quarternumber == 1):
    print('x > 0 and y > 0')
elif(quarternumber == 2):
    print('x < 0 and x > 0')
elif(quarternumber == 3):
    print('x < 0 and y < 0')
elif(quarternumber == 4):
    print('x > 0 and y < 0')
=======
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

with open('file.txt', 'w') as data:
    data.write('0\n')
    data.write('2\n')
    data.write('4\n')
    data.write('6\n')

def fill_list(n):
    return [randint(-n/2, n) for i in range(-n, n + 1)]

def get_data_from_file(path):
    data = open(path, 'r')
    dlist = [int(line.strip()) for line in data]
    data.close()
    return dlist

def get_possition(numbers, datalist):
    mult = 1
    for i in datalist:
        mult *= numbers[i]
    return mult

path = 'file.txt'
n = 6
datalist = get_data_from_file(path)
numbers = fill_list(n)

print(f'Сгенерированный список: {numbers}')
print(f'Заданные элементы в файле: {datalist}')
print(f'Произведение элементов на указанных позицциях: {get_possition(numbers, datalist)}')
>>>>>>> e77508f5901b74bbea075419ce6277b9f23b9102
