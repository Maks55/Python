# Вычислить число с заданной точностью pi
d = input('Введите точность вычисления числа пи: ').split('.')
n = len(d[1])
import math
print('pi = ', round(math.pi, n))