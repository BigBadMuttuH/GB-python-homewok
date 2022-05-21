import math
# Задача 1.
# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# Классическое решение:
# result[]
# for i in range(0, num):
#     if i % 2 == 0:
#         result.append(3**i)
#     else:
#         result.append(-3**i)
# return result
def get_cubs(num):
    return [3**i if i % 2 == 0 else -3**i for i in range(0, num)]


# Задача 2.
# Пользователь задаёт две строки.
# Определить количество вхождений одной строки в другой.
def get_numbers_of_occurrence(str1, str2):
    return str2.count(str1)


# Задача 3.
# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]
def factorial(num):
    return [math.factorial(n) for n in range(1, num + 1)]




# Подсчитать сумму цифр в вещественном числе.
# Классическое решение:
# sum = 0
# for n in str(num):
#     if n not in (',', '.', '-'):
#         sum += int(n)
# return sum
def get_summ_of_numbers(num):
    return sum(map(int, str(num).replace('.', '')))


# print("Задача 1")
# print(get_cubs(5))
#
# print("Задача 2")
# str1 = input("введите 1 строку: ")
# str2 = input("введите 2 строку: ")
# count = get_numbers_of_occurrence(str1, str2)
# print(count)
#
# print("Задача 3")
# print(factorial(4))
# print(factorial(5))

# print("Задача 4")
# print(get_summ_of_numbers(1.5))