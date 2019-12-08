#Задание №2
# Посчитать четные и нечетные цифры введенного натурального числа. Например, если
# введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


def chet_ne_chet(x):
    global chet
    global ne_chet
    cur_chislo = x % 10
    cur_ostatok = x // 10
    if (cur_chislo % 2) == 0:
        chet += 1;
    else:
        ne_chet += 1;
    if cur_ostatok == 0:
        return
    chet_ne_chet(cur_ostatok)


chet = ne_chet = 0;

x = int(input("Введите натуральное число"));
chet_ne_chet(x)
print("Количество четных цифр:", chet);
print("Количество нечетных цифр:", ne_chet);
