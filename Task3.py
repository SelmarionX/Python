# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# *Пример:*

# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06


from msilib import sequence

n = int(input('Введите число: ')) 

def get_sequence(n):
    return [round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]

nums = get_sequence(n)
print(f'Последовательности для {n} --> {nums}')
print(f'Их сумма: {round(sum(nums), 2)}')