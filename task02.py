# Задание №2
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
# числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


array = [float('%.2f'%(random.uniform(0, 49))) for _ in range(10)]
#array = [6, 8, 3, 0, 9, 1, 2, 7, 4, 5]


def merge(a, left, mid, right):
    it1 = 0
    it2 = 0
    result = [0 for _ in range(right-left)]
    while left + it1 < mid and mid + it2 < right:
        if a[left + it1] < a[mid + it2]:
            result[it1 + it2] = a[left + it1]
            it1 += 1
        else:
            result[it1 + it2] = a[mid + it2]
            it2 += 1

    while left + it1 < mid:
        result[it1 + it2] = a[left + it1]
        it1 += 1

    while mid + it2 < right:
        result[it1 + it2] = a[mid + it2]
        it2 += 1

    for i in range(it1 + it2):
        a[left + i] = result[i]

def mergeSort(a):
    i = 1
    while i <= len(a):
        j = 0
        while j <= len(a) - i:
            merge(a,j,j+i,min(j+2*i,len(a)))
            j += 2 * i
        i *= 2

print('Неотсортированный:', array)
mergeSort(array)
print('Отсортированный:', array)