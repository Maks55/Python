# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

number = 20
arr = []
fib = [0, 1]
for i in range(number):
    arr.append(i)

for i in range(2, len(arr)):
    fib.append(fib[i-1] + fib[i-2])

print(fib)
