# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# Последняя строка содержит число X


list_1 = []
n = int(input("введите кол-во элементов массива: "))
for i in range(n):
    list_1.append(int(input(f'Введите {i+1} элемент массива: ')))

x = int(input("введите искомое число: "))

listDif = [abs(x - i) for i in list_1]
resultIndex = listDif.index(min(listDif))
print(f'{list_1[resultIndex]} - ближайшее число к искомому')