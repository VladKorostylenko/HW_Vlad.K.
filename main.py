# 1. Напишите функцию calculations () так, чтобы она могла принимать две переменные и вычислять их сложение и вычитание.
# А также он должен возвращать как сложение, так и вычитание за один вызов возврата.
#
# def calculations(x, y):
#     def sum_n(x, y):
#         return x + y
#     def sub_n(x, y):
#         return x - y
#     return sum_n(x, y), sub_n(x, y)
#
# z = calculations(5, 2)
#
# print(z)
#
# 2. Напишите функцию Python для суммирования всех чисел в списке.
#
# def sum_numbers(numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total
#
# z = sum_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#
# print(z)

# 3. Напишите функцию func () так, чтобы она могла принимать аргументы переменной длины и выводить все значения аргументов с индексом аргумента.
#
# def func(*y):
#     x = {}
#     z = 0
#     for _ in y:
#         x[z] = y[z]
#         z += 1
#     return x
#
# print(func(1, 2, 3, 4, 5))
#
# 4. Создайте функцию showEmployee () таким образом, чтобы она принимала имя сотрудника и его зарплату и отображала и то, и другое.
# Если в вызове функции отсутствует зарплата, присвойте зарплате значение по умолчанию 9000.
#
# def showEmployee(name, *sallary):
#     if len(sallary) == 0:
#         sallary = 9000
#
#     return name, sallary[0]
#
# print(showEmployee("Иван", 10000))
#
# 5. Дано натуральное число N. Вычислите сумму его цифр. Напишите рекурсивную функцию
#
# def rec_func(num):
#     return num%10 + sum_digits(num//10) if num > 9 else num
#
# print(rec_func(123))
#
# 6. Напишите рекурсивную функцию для вычисления числа Фибоначи
#
# def fibonachi(n):
#     return n - 1 if n < 3 else fibonachi(n - 2) + fibonachi(n - 1)
#
# n = int(input("\nВведите порядковый номер числа Фибоначчи: "))
# print(f"Число Фибоначчи номер {n} равно {fibonachi(n)}")

# 7. Напишите функцию для умножения всех чисел в списке. Рекурсивно
#
# import random
#
# LIST_MAX_LEN = 7
# ELEM_NUM_MIN = 1
# ELEM_NUM_MAX = 20
# def multi_list(lst, n=0):
#     return 1 if n >= len(lst) else lst[n] * multi_list(lst, n + 1)
#
#
# list_orig = [random.randint(ELEM_NUM_MIN, ELEM_NUM_MAX) for _ in range(0, random.randint(2, LIST_MAX_LEN))]
# print(f"Список: {list_orig}")
# print(f"Произведение чисел из списка: {multi_list(list_orig)}")
#
# 8. Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае. 8 - YES, 3 - NO
#
# def is_power_2(num):
#     if num == 2:
#         return 'YES'
#     elif num % 2 == 1:
#         return 'NO'
#     else:
#         return is_power_2(num // 2)
#
#
# n = int(input("\nВведите натуральное n = "))
# print(f'\33[34mТочная степень двойки: {is_power_2(n)}')
# 9. Создайте inner функцию для вычисления сложения следующим образом:
# * Создайте внешнюю функцию, которая будет принимать два параметра, a и b
# * Создайте внутреннюю функцию внутри внешней функции, которая будет вычислять сложение a и b
# * Наконец, внешняя функция добавит 5 и вернет ее.
#
#
# a = int(input("\nВведите a = "))
# b = int(input("Введите b = "))
#
#
# def inner(x, y):
#     def sumxy():
#         return x + y
#
#     return sumxy() + 5
#
#
# print(f'\33[34mInner сумма a и b = {inner(a, b)}')
