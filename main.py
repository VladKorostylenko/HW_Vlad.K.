# 1. За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# Программа получает на вход числа n и m.

# total_distance = int(input("Введите общее расстояние, км: "))
#
# distance_per_day = int(input("Введите кол-во километров, которое машина проезжает за день, км: "))
#
# if total_distance > 0 or distance_per_day > 0:
#     amount_of_days = int(total_distance/distance_per_day)
#     amount_of_hours = int((total_distance%distance_per_day)/distance_per_day*24)
#
#     print (f"Чтобы проехать {total_distance}км, машине понадобится {amount_of_days}д. {amount_of_hours} ч.")
# else total_distance <= 0 or distance_per_day <= 0:
#     print ("Значение должно быть больше 0. Пожалуйста, попробуйте снова.")

# 2. Пользователь вводит трехзначное число. Найдите сумму его цифр. (используйте %)
#
# three_digit_number = int(input("Введите целое, трехзначное число: "))
#
# if 100 <= three_digit_number <= 999:
#     left_from_100 = int(three_digit_number//100)
#     left_from_10 = int(three_digit_number%100//10)
#     left_from_1 = int(three_digit_number%100%10)
#
#     sum_of_numbers = int(left_from_100 + left_from_10 + left_from_1)
#
#     print (f"Сумма трех цифр из числа {three_digit_number} равна: {sum_of_numbers}")
#
# elif three_digit_number <= 99 or three_digit_number >= 1000:
#     print ("Пожалуйста, используйте только трехзначные числа")

# 3. Найти максимальное число из трех. Числа вводится с клавиатуры
#
# first_number = int(input("Введите первое число: "))
#
# second_number = int(input("Введите второе число: "))
#
# third_number = int(input("Введите третье число: "))
#
# if first_number >= second_number and first_number >= third_number:
#     print (f"Наибольшее число: {first_number}")
#
# elif second_number >= first_number and second_number >= third_number:
#     print(f"Наибольшее число: {second_number}")
#
# else third_number >= first_number and third_number >= second_number:
#     print(f"Наибольшее число: {third_number}")

# 4. Определить високосный год или нет.Число вводится с клавиатуры

# input_year = int(input("Введите год: "))
#
# if input_year % 4 == 0:
#     print("Год высокостный")
# else:
#     print("Год не высокостный")
#
# # 5. Определить четное или нечетное число. Число вводится с клавиатуры

# input_number = int(input("Введите число: "))
#
# if input_number % 2 == 0:
#     print("Число четное")
# else:
#     print("Число не четное")

#  Задания с повышенной сложностью на 100 баллов

# 6. Найти корни квадратного уравнения и вывести их на экран, если они есть. Если корней нет,
# то вывести сообщение об этом.
# Конкретное квадратное уравнение определяется коэффициентами a, b, c, которые вводит пользователь.

# print('Решаем уравнение a•x²+b•x+c=0')
#
# koef_a = input("Введите число a: ")
# koef_b = input("Введите число b: ")
# koef_c = input("Введите число c: ")
#
# koef_a = float(koef_a)
# koef_b = float(koef_b)
# koef_c = float(koef_c)
#
# discriminant = koef_b**2 - 4*koef_a*koef_c
# print('Дискриминант = ' + str(discriminant))
# if discriminant < 0:
#     print('Корней нет')
# elif discriminant == 0:
#     x = -koef_b / (2 * koef_a)
#     print('x = ' + str(x))
# else:
#     x1 = (-koef_b + discriminant ** 0.5) / (2 * koef_a)
#     x2 = (-koef_b - discriminant ** 0.5) / (2 * koef_a)
#     print("x₁ = " + str(x1))
#     print("x₂ = " + str(x2))


# 7. Дана следующая функция y=f(x):
# y = 2x – 10, если x > 0
#
# y = 0, если x = 0
#
# y = 2 * |x| – 1, если x < 0
#
# Найти значение функции по x, который вводиться с клавиатуры
#
# x = int(input("Введите значение х: "))
#
# if x > 0:
#     y = 2 * x - 10
#     print(y)
# elif x == 0:
#     y = 0
#     print(y)
# else:
#     y = 2 * x - 1
#     print(y)

