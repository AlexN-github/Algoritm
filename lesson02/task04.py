#Задание #4
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество
# элементов (n) вводится с клавиатуры.

def element(r,k):
    if k == 0:
        return r
    else:
        r = r / 2
        if r % 2 != 0:
            r = r * (-1)
        return(element(r,k-1))


s = 0
n = int(input("Введите значение n"));
for i in range(n):
    s += element(1,i)
print(s)
