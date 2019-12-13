# Задание №2
# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив
# надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

array1 = [4,6,3,6,8,5,9,34,57,78,44,23,55,62]
array2 = []
for inx, val in enumerate(array1):
    if val % 2 == 0:
        array2.append(inx)

print("Искомый массив: ", array2)