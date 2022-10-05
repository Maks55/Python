# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

lst = [11, 34, 12, 23]
revlst = list(reversed(lst))
newlst=[]
for i in range(len(lst)):
    newlst.append (lst[i] * revlst[i])
print(newlst[0:2])