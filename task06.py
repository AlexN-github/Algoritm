# Задание №6
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

def get_MaxMin_Inx(source_array):
    max_inx = min_inx = 0
    for inx, val in enumerate(source_array[1:], 1):
        if val > source_array[max_inx]:
            max_inx = inx
        if val < source_array[min_inx]:
            min_inx = inx
    return {'max_inx': max_inx, 'min_inx': min_inx}


size_array = 10
array = [random.randint(1,50) for _ in range(size_array)]
print(array)
res = get_MaxMin_Inx(array)
print(res)
sum_ = 0
if res["max_inx"] > res["min_inx"]:
    range_start = res["min_inx"] + 1
    range_end = res["max_inx"]
else:
    range_start = res["max_inx"] + 1
    range_end = res["min_inx"]
for i in array[range_start:range_end]:
    sum_ += i
print("Требуемая сумма:", sum_)
