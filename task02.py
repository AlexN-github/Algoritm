# Задание №2
# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число
# представляется как массив, элементы которого — цифры числа. Например, пользователь
# ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел
# из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

import collections


def get_dict(str_):
    counter = collections.Counter()
    len_str = len(str_)
    for i in range(len_str):
        counter[i] = int(str_[len(str_) - i - 1], 16)  # int(str_[i])
    return counter

def get_hex_result(coll):
    perenos = 0; res = ""
    for i in coll:
        coll[i] = coll[i] + perenos
        if coll[i] > 16:
            perenos = coll[i] // 16
            coll[i] = coll[i] % 16
        else:
            perenos = 0
        res = hex(coll[i])[2:].upper() + res
    else:
        if perenos > 0:
            res = hex(perenos)[2:].upper() + res
    return res

def addition(x1,x2):
    sum_coll = get_dict(x1) + get_dict(x2)
    return get_hex_result(sum_coll)

def mult(x1,x2):
    count1 = get_dict(x1)
    count2 = get_dict(x2)
    counter = collections.Counter()
    for i in count1:
        for j in count2:
            counter[j+i] = counter[j+i] + count1[i]*count2[j]
    return get_hex_result(counter)

x1 = input("Введите первое шестнадцатиричное число")
x2 = input("Введите второе шестнадцатиричное число")

print("Сумма:", addition(x1, x2))

print("Произведение:", mult(x1, x2))

