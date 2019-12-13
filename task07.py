# Задание №7
# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны
# между собой (оба являться минимальными), так и различаться.

source_array = [4,6,3,6,8,5,9,34,57,78,1,23,8,62]
print(source_array)
array = source_array.copy()
min_ = []
for i in range(0, 2):
    min_.append(array[0])
    min_inx = 0
    for inx,val in enumerate(array[1:],1):
        if val < min_[-1]:
            min_[-1] = val
            min_inx = inx
    del array[min_inx]
print(min_)
