# Задайте список из чисел n последовательности ((1+1/n))**n 

n = int(input("Введите число "))
p = 0
for i in range (1, n+1):
    p = p + (1 + 1/i) ** i
print (p)

