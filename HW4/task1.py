# Вычислить число c заданной точностью d
# Пример:
#  - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

n = int(input("Введите натуральное число, для вывода точности значения π : "))
a = math.pi
template = '{:.' + str(n) + 'f}'
print(template.format(a))

