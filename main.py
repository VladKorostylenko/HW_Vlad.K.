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
# def rec_func(N):
#     return N%10 + sum_digits(N//10) if N > 9 else N
#
# print(rec_func(123))
#
# 6. Напишите рекурсивную функцию для вычисления числа Фибоначи
#
# Вариант для поиска конкретного числа.
# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# fibonacci_list_index = int(input("Введите порядковый номер числа из ряда Фибоначчи, которое вы хотите получить:" ))
#
# print(f"Число fibonacci(fibonacci_list_index))

# 7. Напишите функцию для умножения всех чисел в списке. Рекурсивно

# def mult_list(list):
#     if list == 1:
#         return list
#     else:
#         return list[-1] * mult_list(list[0]),
#
#
# print(mult_list([1, 2, 3, 4]))
#
def multiply(lst):
    if lst == 0:
        return 0
    else:
        index = 0
        return lst[index] * multiply(lst)

lst = [1, 2, 3, 4, 5, 6]

print(multiply(lst))

# 8. Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае. 8 - YES, 3 - NO
# #
# 9. Создайте inner функцию для вычисления сложения следующим образом:
# * Создайте внешнюю функцию, которая будет принимать два параметра, a и b
# * Создайте внутреннюю функцию внутри внешней функции, которая будет вычислять сложение a и b
# * Наконец, внешняя функция добавит 5 и вернет ее.