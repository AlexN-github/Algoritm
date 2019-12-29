# Задание №2
# Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter
from collections import namedtuple
import heapq

#Класс промежуточного узла
class Node(namedtuple("Node", ["left","right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")
#Класс конечного листа
class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"

def huf_encode(s):
    #Создаем первоначальный список с листями
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    # Используем очередь с приоритетами (кучи).
    # Помещаем список листьев в очередь
    heapq.heapify(h)
    count = len(h)
    #Строим дерево
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    #Обходим дерево и кодируем листья
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return  code




s = "HHHHello World!!!"
print("Исходная строка:", s)
code = huf_encode(s)
#print([code[ch] for ch in s])
encoded = "".join(code[ch] for ch in s)

# Сортируем список закодированных символов в порядке увеличения длинны кода
# и выводим на экран
for item in sorted(code.items(), key=lambda x: len(x[1])):
    print("{}: {}".format(item[0], item[1]))
print("Закодированная строка:", encoded)




