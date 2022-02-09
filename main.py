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
# sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
#
# new_list = []
# x = 0
# y = -1
#
# for item in sample_list:
#     new_list.append(list(item))
#     new_list[x][y] = 100
#     new_list[x] = tuple(new_list[x])
#     x += 1
#
# print(new_list)
#
# 3. Напишите программу для поэлементного вычисления суммы заданных кортежей. Результатом должен быть кортеж.
#
# Input
#
# tup1 = (1, 2, 3, 4)
# tup2 = (3, 5, 2, 1)
# tup3 = (2, 2, 3, 1)
# #
# # Output
# #
# # (6, 9, 8, 6)
#
# list4 = []
# tup4 = ()
#
# i = 0
#
# list1 = list(tup1)
# list2 = list(tup2)
# list3 = list(tup3)
#
# for _ in list1:
#     list4.append(list1[i] + list2[i] + list3[i])
#     i += 1
#
# tup4 = tuple(list4)
#
# print(tup4)

# 4. Напишите программу, которая проверяет, присутствует ли А в наборе или нет. А вводится с клавиатуры
#
import random

print("Сгенерируйте свой набор")

set_size = int(input("Введите кол-во символов в наборе: "))
random_upper_bound = int(input("Введите макисмальный размер числа: "))

set1 = set()

for _ in range(0, set_size):
    set1.add(random.randint(0, random_upper_bound))

print(f"Список в котором бутет проверяться наличие числа: {set1}")

a_number = int(input("Введите целое число, присутсвие которого вы хотите проверить в наборе: "))

flag = 0

for set_number in set1:
    if set_number == a_number:
        flag +=1

if flag > 0:
    print(f"Число {a_number} есть в списке - {set1}, в кол-ве {flag} штук.")
else:
    print(f"Число {a_number} отсутствует в списке - {set1}")

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