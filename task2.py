# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# Пример:
# N = 20 => [2, 2, 5]

n = int(input('Введите натуральное число: '))
a = 2
arr = []
while n != 1:
    if n % a == 0:
        arr.append(a)
        n = n / a
        a = 1
    a += 1
print(arr)
