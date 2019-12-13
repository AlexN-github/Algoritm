# Задание №4
# Определить, какое число в массиве встречается чаще всего.

number = {
    "num" : 0,
    "count" : 0
}
array = [45, 44, 47, 9, 47, 9, 44, 28, 41, 9]
for inx, val in enumerate(array[:-1]):
    cur_count = 1
    for inx_, val_ in enumerate(array[inx+1:],inx+1):
        if val == val_:
            cur_count += 1;
    if cur_count > number["count"]:
        number["num"] = val
        number["count"] = cur_count
print("Максимальное число:", number["num"],"\nВстречается:",number["count"])

