# Реализуйте алгоритм перемешивания списка
import random
arr = [1,2,3,4,5,6,7,8]
arrnew=[]
for x in range(len(arr)):
    arrnew.append (random.choice(arr))
print(arrnew)
