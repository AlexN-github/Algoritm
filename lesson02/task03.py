#Задание №3
# Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран. Например, если введено число 3486, надо вывести 6843.

def Reverse(x):
    global Rev;
    cur_chislo = x % 10;
    cur_ostatok = x // 10;
    Rev = Rev*10+cur_chislo
    if cur_ostatok == 0:
        return cur_chislo
    else:
        Reverse(cur_ostatok);


x = int(input("Введите натуральное число"));
Rev = 0;
Reverse(x);
print(Rev);