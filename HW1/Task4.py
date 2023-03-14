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
    
#     number = input()
# if (number == '1'):
#     print("(X >0 и Y > 0)")
# elif (number == '2'):
#     print("(X >0 а Y < 0)")
# elif (number == '3'):
#     print("(X < 0 и Y < 0)")
# elif (number == '4'):
#     print("(X > 0 и Y < 0)")
# else:
#     print("Неправильный ввод")

