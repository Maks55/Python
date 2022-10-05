# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def bin(x):
    if x == 0:
        return 0
    res = ""
    while x>0:
        if x % 2 == 0:
            res = '0'+ res
        else:
             res = '1' + res
        x = x // 2
    return res

print(bin(45))