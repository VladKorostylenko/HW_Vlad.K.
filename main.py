# 1.Напишите программу для преобразования списка в кортеж
#
# import random
#
# list_size = int(input("Введите кол-во символов в списке: "))
# random_upper_bound = int(input("Введите макисмальный размер числа: "))
#
# list1 = []
#
# for _ in range(0, list_size):
#     list1.append(random.randint(0, random_upper_bound))
#
# tuple1 = tuple(list1)
#
# print(list1)
#
# print(tuple1)
#
# print(type(tuple1))
#
# 2. Напишите программу для замены последнего значения кортежей в списке
#
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
#
sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

new_list = []
x = 0
y = -1

for item in sample_list:
    new_list.append(list(item))
    new_list[x][y] = 100
    x += 1





print(new_list)
#
#
#
# 3. Напишите программу для поэлементного вычисления суммы заданных кортежей. Результатом должен быть кортеж.
#
#
#
# Input
#
# (1, 2, 3, 4)
#
# (3, 5, 2, 1)
#
# (2, 2, 3, 1)
#
#
#
# Output
#
# (6, 9, 8, 6)
#
#
#
# 4. Напишите программу, которая проверяет, присутствует ли А в наборе или нет. А вводится с клавиатуры
#
# 5. Напишите программу, чтобы проверить, не имеют ли два заданных набора (set) общих элементов.
#
# 6. Напишите программу для поиска элементов в данном наборе A (set), которых нет в другом наборе B.
#
# 7. Напишите программу, которая удаляет пересечение 2-го набора из 1-го набора.
#
#
#
# 8. Реализовать логику Union для двух списков (list), проверить работу алгоритма на set.union
#
# 9. Реализовать логику Difference для двух списков (list), проверить работу алгоритма на set.difference