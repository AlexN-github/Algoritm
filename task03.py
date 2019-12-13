# Задание №3
# В массиве случайных целых чисел поменять местами минимальный и максимальный
# элементы.

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
source_array = [random.randint(1,50) for _ in range(size_array)]

res = get_MaxMin_Inx(source_array)
result_array = source_array.copy()
result_array[res["min_inx"]] = source_array[res["max_inx"]]
result_array[res["max_inx"]] = source_array[res["min_inx"]]

print("Минимальное:", source_array[res["min_inx"]], "\nМаксимальное:", source_array[res["max_inx"]])
print(source_array)
print(result_array)