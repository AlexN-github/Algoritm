# Задание №1
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для
# всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже
# среднего.

import collections

n = int(input("Введите количество предприятий"))
ent = collections.defaultdict(list)
for i in range(n):
    name = input('Введите название предприятия №{0} '.format(i))
    for j in range(4):
        prib = int(input('Введите прибыль за квартал №{0} '.format(j)))
        ent[name].append(prib)
    avg_arr = [sum(ent[x])/4 for x in ent]
    avg =  sum(avg_arr)/n
print("Средняя прибыль предприятий за год:", avg)
print("Список предприятий прибыль выше среднего:")
print([x for x in ent if sum(ent[x])/4 > avg])
print("Список предприятий прибыль меньше среднего:")
print([x for x in ent if sum(ent[x])/4 < avg])
