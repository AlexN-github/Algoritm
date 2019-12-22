# Задание №1
# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
# программах в рамках первых трех уроков. Проанализировать результат и определить
# программы с наиболее эффективным использованием памяти.


# Задание
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два
# абсолютно разных значения.

import sys

def show_size(x):
    s = sys.getsizeof(x)
    #print(f'type={type(x)}, size={s}, obj={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                s += show_size(key)
                s += show_size(value)
        elif not isinstance(x, str):
            for item in x:
                s += show_size(item)
    return s

# Вариант №1
# Последовательно перебираем все элементы, ищем в них отрицательные и запоминаем наиболее максимальное
def get_max_min_1(array):
    max_ = None
    for inx, val in enumerate(array[:-1]):
        if val < 0:
            if max_ is None or val > max_:
                max_ = val
    print("###########Оцениваем размер переменных Вариант №1")
    vars_ = [(x[0], show_size(x[1])) for x in list(locals().items()) if x[0].startswith("__") == 0]
    [print(f"Переменная: {x[0]}, Размер: {x[1]}") for x in vars_]
    print(f"Суммарный размер всех переменных: {sum([x[1] for x in vars_])}")
    print("#"*50)

    return max_


# Вариант №2
# Находим все отрицательные числа и находим максимальное среди них, используя встроенную функцию

def get_max_min_2(array):
    neg_array = [x for x in array if x < 0]
    print("###########Оцениваем размер переменных Вариант №2")
    vars_ = [(x[0], show_size(x[1])) for x in list(locals().items()) if x[0].startswith("__") == 0]
    [print(f"Переменная: {x[0]}, Размер: {x[1]}") for x in vars_]
    print(f"Суммарный размер всех переменных: {sum([x[1] for x in vars_])}")
    print("#"*50)
    return max(neg_array)


# Вариант №3
# Сортируем исходный массив по возврастанию и ищем методом половинного деления переход с отрицательного
# на положительное

def get_max_min_3(array):
    a = sorted(array)
    pos = len(a) // 2
    while ((a[pos] >= 0 )and a[pos-1] <= 0 or a[pos] <= 0 and a[pos-1] >= 0) == False:
        if a[pos] > 0:
            a = a[:pos]
        else:
            a = a[pos:]
        pos = len(a) // 2

    print("###########Оцениваем размер переменных Вариант №3")
    vars_ = [(x[0], show_size(x[1])) for x in list(locals().items()) if x[0].startswith("__") == 0]
    [print(f"Переменная: {x[0]}, Размер: {x[1]}") for x in vars_]
    print(f"Суммарный размер всех переменных: {sum([x[1] for x in vars_])}")
    print("#"*50)

    if a[pos] < 0:
         return a[pos]
    else:
        return a[pos-1]



#####################
# Результаты
import random

n = int(input("Введите размер массива случайных чисел:"))

array = [random.randint(-n,n) for _ in range(n)]
print(array)
print("Выполняем Вариант№1:")
print("Максимальное отрицательное число:", get_max_min_1(array))
print("\nВыполняем Вариант№2:")
print("Максимальное отрицательное число:", get_max_min_2(array))
print("\nВыполняем Вариант№3:")
print("Максимальное отрицательное число:", get_max_min_3(array))



# Вывод:
# ОС Windows 10 - 64bit
# Python Pycharm - 64bit
# Python interpreter - 32bit

# Размера исходного массива n = 1000,
# Наихудший вариант №2 потому что, там создается дополнительный список
# отрицательных элементов. Вариант №1 и №2 примерно одинаковые по
# затратам на память

# Выполняем Вариант№1:
# Суммарный размер всех переменных: 18554

# Выполняем Вариант№2:
# Суммарный размер всех переменных: 27610

# Выполняем Вариант№3:
# Суммарный размер всех переменных: 18630