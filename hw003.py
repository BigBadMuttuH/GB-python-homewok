import math
import numbers
from random import randint


def get_least_common_multiple(a, b):
    """
    Найти НОК двух чисел,
    классический вариант решения
    :param: tow int numbers a, b
    :return: common multiple of tow numbers
    """
    if a == 0 or b == 0:
        return 0
    lcm = min(a, b)
    # print(f"{a=}, {b=}, {lcm=}")
    while True:
        if lcm % a == 0 and lcm % b == 0:
            break
            print(f"{a=}, {b=}, {lcm=}")
        lcm += 1
    return lcm


def glcm_math(a, b):
    """
    Найти НОК двух чисел
    Вариант через math.gcd() находим общий делитель
    далее по формуле lcm(a, b) = (a * b) // math.gcd(a, b)
    :param: tow int numbers a, b
    :return: common multiple of tow numbers
    """
    return ((a * b) // math.gcd(a, b))


# a, b = map(int, input("Введите два числа (через пробел): ").strip().split())
# print(f"НОК чисел {a=} и {b=} = {get_least_common_multiple(a, b)}")
# print(f"НОК чисел {a=} и {b=} = {glcm_math(a, b)}\n")


def get_PI(d):
    """
    Вычислить число Пи c заданной точностью d
    Пример: при d = 0.001,  c= 3.141.
    по формуле Лейбница
    :param: int d - точность вычисления
    :return: PI
    """
    k = 1
    sum = 0
    for i in range(10_000):
        if i % 2 == 0:
            sum += 4 / k
        else:
            sum -= 4 / k
        k += 2
    return "{:1.{poins}f}".format(sum, poins=int(d))


# a = input("Введите точность для PI(количество знаков после запятой): ")
# print(get_PI(a))

def get_simple_multipliers(num):
    """
    список простых множителей натурального числа N
    :param: int
    :return: list
    """
    return [i for i in range(1, num + 1) if num % i == 0]

# n = int(input("число: "))
# print(get_simple_multipliers(n))


def get_unique_list(nlist: list):
    """
    Дана последовательность чисел.
    Получить список неповторяющихся элементов исходной последовательности
    Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]
    преобразуем список во множество, и дальше в обратно в list
    :param nlist: type list
    :return: list
    """
    return list(set(nlist))


random_list = [randint(1, 10) for i in range(1, 21)]
# print(random_list)
# print(get_unique_list(random_list))


def create_file(count: int):
    """
    Дан текстовый файл, содержащий целые числа.
    :param count: int - количество чисел
    :return: numbers.txt
    """
    numbers = [randint(1, 100) for _ in range(1, count)]
    with open("numbers.txt", "w") as file:
        for num in numbers:
            file.write(f"{num}\n")

# create_file(100)


def remove_even_numbers_from_file(file_name: str):
    """
    Удалить из него все четные числа.
    :param file:
    :return: numbers.txt
    """
    numbers = []
    with open(file_name, "r") as file:
        for item in file:
            num = int(str(item).split('\n')[0])
            if num % 2 == 0:
                numbers.append(num)
    print(numbers)
    with open(file_name, 'w') as file:
        for num in numbers:
            file.write(f"{num}\n")


# remove_even_numbers_from_file("numbers.txt")
