# Задание №3
# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве
# медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся
# элементы, которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также
# недопустима).


import random

m = int(input('Введите m'))
array = [random.randint(0, 10) for _ in range(2*m+1)]
print(array)

#array = [6, 0, 3, 9, 4, 4, 4, 4, 5]

for inx_i,i in enumerate(array):
    count_l = 0; count_g = 0; count_e = 0;
    for inx_j,j in enumerate(array):
        if inx_i != inx_j:
            count_l += 1 if i < j else 0
            count_g += 1 if i > j else 0
            count_e += 1 if i == j else 0
    if count_l == count_g or min(count_l, count_g)+count_e >= max(count_l, count_g):
        print('Медина: ', i)
        break

