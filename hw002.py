import math

# Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4
def get_sum_of_odd_numbers(numbers):
    print(f"дан список: {numbers}")
    # list_of_odd_numbers = numbers[::2]
    return sum(numbers[::2])
    # классическое решение
    # sum = 0
    # i = 0
    # while i < len(numbers):
    #     sum += numbers[i]
    #     i += 2
    # return sum

list_of_numbers1 = [n for n in range(1, 10)]
print(f"сумма элементов стоящих на нечетной позиции ="
      f" {get_sum_of_odd_numbers(list_of_numbers1)}\n")


# Найти произведение пар чисел в списке.
# Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]
def get_multiplications(numbers):
    print(f"дан список: {numbers}")
    size = math.ceil(len(numbers)/2)
    return [numbers[i] * numbers[len(numbers) - i - 1] for i in range(size)]

list_of_numbers2 = [2, 3, 4, 5, 6]
list_of_numbers3 = [2, 3, 5, 6]
print(f"список из произведений пар чисел = "
      f"{get_multiplications(list_of_numbers1)}\n")

print(f"список из произведений пар чисел = "
      f"{get_multiplications(list_of_numbers2)}\n")

print(f"список из произведений пар чисел = "
      f"{get_multiplications(list_of_numbers3)}\n")


# В заданном списке вещественных чисел
# найдите разницу между максимальным и минимальным значением
# дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
def get_diff_between_point_numbers(numbers):
    print(f"дан список: {numbers}")
    min = max = round(math.modf(numbers[0])[0], 4)
    for number in numbers:
        num = round(math.modf(number)[0], 4)
        if max < num:
            max = num
        if num != 0 and min > num:
            min = num

    return max - min

list_of_numbers4 = [1.1, 1.2, 3.1, 5, 10.01]
print(f"разница между максимальным и минимальным значением дробной части элементов списка = "
      f"{get_diff_between_point_numbers(list_of_numbers4)}\n")


# Написать программу преобразования десятичного числа в двоичное.
def decimal_to_binary(number):
    # return bin(number)[2:]
    binary = ''
    if number == 0: return '0'
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    return binary

print(decimal_to_binary(10))
print(decimal_to_binary(0))
print(decimal_to_binary(3))
