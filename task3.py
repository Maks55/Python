# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


arr = [1.5, 2.3, 4.7, 6.4]
newarr = [int((i*10) % 10) for i in arr]
max = newarr[0]
min = newarr[0]

for i in range(len(newarr)):
    if max < newarr[i]:
        max = newarr[i]
    if min > newarr[i]:
        min = newarr[i]
print (max - min)
