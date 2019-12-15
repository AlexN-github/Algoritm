# Задание №2
# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и
# возвращать соответствующее простое число. Проанализировать скорость и
# сложность алгоритмов.

# Вариант №1
# Классический алгоритм Решето Эратосфена

def get_simple_number_erato1(n):
    #Функция прокалывает дырки
    def prokalyvaem_dyrki(arr, n): # передаем масив и простое число
        start_search = n*2
        for inx,digit in enumerate(arr[start_search::n],n):
            for inx, digit in enumerate(arr[start_search::n], n):
                full_inx = arr.index(digit)
                if arr[full_inx] != 0:  # если он не равен нулю, то
                    arr[full_inx] = 0
        return arr

    lst = []
    arr = []
    arr.append(0); arr.append(0)   # заполняем первый и второй нулями
    while len(lst) != n:
        arr.append(len(arr))
        for inx,a in enumerate(arr[2:], 2):
            if arr[inx] != 0:  # если он не равен нулю, то мы нашли простое число и:
                prokalyvaem_dyrki(arr, a)
        lst = [x for x in arr if x != 0]

    return lst[-1]



# Вариант №2
# Оптимизированный алгоритм Решето Эратосфена
# Начинаем попроверять не с n*2, а с n**2



def get_simple_number_erato2(n):
    #Функция прокалывает дырки
    def prokalyvaem_dyrki(arr, n): # передаем масив и простое число
        start_search = n**2
        for inx,digit in enumerate(arr[start_search::n],n):
            for inx, digit in enumerate(arr[start_search::n], n):
                full_inx = arr.index(digit)
                if arr[full_inx] != 0:  # если он не равен нулю, то
                    arr[full_inx] = 0
        return arr

    lst = []
    arr = []
    arr.append(0); arr.append(0)   # заполняем первый и второй нулями
    while len(lst) != n:
        arr.append(len(arr))
        for inx,a in enumerate(arr[2:], 2):
            if arr[inx] != 0:  # если он не равен нулю, то мы нашли простое число и:
                prokalyvaem_dyrki(arr, a)
        lst = [x for x in arr if x != 0]

    return lst[-1]



# Вариант №3
# Поиск простых чисел не используя алгоритм Решето Эротасфена

def get_simple_number(n):
    lst = [2]
    i = 3
    while len(lst) != n:
        for j in lst:
            if j**2-1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
        i +=2
    return lst[-1]



# Оцениваем алгоритмы
import timeit
import cProfile

n = int(input("Введите порядковый номер простого числа:"))

s = """
num = get_simple_number_erato1(n)
"""
#print("Алгоритм Эр.№1. Простое число:", num)
print(timeit.timeit(s,number=50,globals=globals()))

s = """
num = get_simple_number_erato2(n)
"""
#print("Алгоритм Эр.№2. Простое число:", num)
print(timeit.timeit(s,number=50,globals=globals()))

s = """
num = get_simple_number(n)
"""
#print("Алгоритм не Эр. Простое число:", num)
print(timeit.timeit(s,number=50,globals=globals()))
