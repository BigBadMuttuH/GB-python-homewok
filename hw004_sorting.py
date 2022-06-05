import random
from random import randint
from timeit import default_timer as timer
import functools


def measure_time(func, currently_evaluating=set()):
    """ декоратор для подсчета времени выполнения функции """

    @functools.wraps(func)
    def inner(*args, **kwargs):
        if func in currently_evaluating:
            return func(*args, **kwargs)
        else:
            start_timer = timer()
            currently_evaluating.add(func)
            try:
                result = func(*args, **kwargs)
            finally:
                currently_evaluating.remove(func)
            end_timer = timer()
            print(f"Function {func.__name__} took {end_timer - start_timer} for execution")
            return result

    return inner


def save_to_file(file_name="numbers.txt", list_of_data=[]):
    """ Запись данных в файл
    :param file_name: название файла
    :param list_of_data: набор значений (list)
    """
    with open(file_name, 'w') as file:
        for item in list_of_data:
            file.write(f"{item}\n")


def load_from_file(file_name="numbers.txt", list_of_data=[]):
    """ Чтение данных из файла
    :param file_name: название файла
    :param list_of_data: набор значений (list)
    """
    with open(file_name, "r") as file:
        for item in file:
            num = int(str(item).split('\n')[0])
            list_of_data.append(num)
    return list_of_data


@measure_time
def bubble_sort(list_of_data: list):
    """ Классическая сортировка пузырьком
    :param list_of_data: list
    :return: list
    """
    for i in range(0, len(list_of_data) - 1):
        for j in range(0, len(list_of_data) - 1):
            if list_of_data[j] > list_of_data[j + 1]:
                tmp = list_of_data[j]
                list_of_data[j] = list_of_data[j + 1]
                list_of_data[j + 1] = tmp
                # print(f"{tmp=}, {list_of_data[j]}=, {list_of_data[j + 1]}")
    return list_of_data


@measure_time
def smart_bubble_sort(list_of_data: list):
    """ Оптимизированная сортировка пузырьком.
    Проверяем произошел ли swap
    :param list_of_data: list
    :return: list
    """
    swap = True
    iterations = 0
    while swap:
        swap = False
        for i in range(0, len(list_of_data) - iterations - 1):
            if list_of_data[i] > list_of_data[i + 1]:
                # swap
                list_of_data[i], list_of_data[i + 1] = list_of_data[i + 1], list_of_data[i]
                swap = True
        iterations += 1
    print(f"{iterations=}")
    return list_of_data


@measure_time
def quick_sort(list_of_data: list):
    """ Быстрая сортировка (Чарьза Хоара). Выбираем один опорный элемент из списка.
    А всё остальное передвигаем так, чтобы этот элемент встал на своё место.
    Все элементы меньше него перемещаются влево, а равные и большие элементы перемещаются вправо.
    :param list_of_data: list
    :return: list
    """
    if len(list_of_data) <= 1:
        return list_of_data
    else:
        support_element = random.choice(list_of_data)

        small_elements_list = []
        big_elements_list = []
        equal_elements_list = []
        for num in list_of_data:
            if num < support_element:
                small_elements_list.append(num)
            elif num > support_element:
                big_elements_list.append(num)
            else:
                equal_elements_list.append(num)
        return quick_sort(small_elements_list) \
               + equal_elements_list \
               + quick_sort(big_elements_list)


@measure_time
def quick_sort_opt(list_of_data):
    """Оптимизированная быстрая сортировка"""
    if len(list_of_data) <= 1:
        return list_of_data
    else:
        support_element = random.choice(list_of_data)

    small_elements_list = [n for n in list_of_data if n < support_element]
    equal_elements_list = [support_element] * list_of_data.count(support_element)
    big_elements_list = [n for n in list_of_data if n > support_element]

    return quick_sort_opt(small_elements_list) \
           + equal_elements_list \
           + quick_sort_opt(big_elements_list)


# Создать и заполнить файл случайными целыми значениями.
save_to_file(list_of_data=[randint(-100, 100) for _ in range(1, 20_000)])
data = load_from_file(list_of_data=[])
# Выполнить сортировку содержимого файла по возрастанию.
print(f"Сортировка пузырьком")
print(data)
print(bubble_sort(data))

print(f"\nСортировка пузырьком с проверкой замены значений и подсчетом итераций")
data = load_from_file(list_of_data=[])
print(data)
print(smart_bubble_sort(data))

print(f"\nБыстрая сортировка (Хоара)")
data = load_from_file(list_of_data=[])
print(data)
print(quick_sort(data))

print(f"\nОптимизированная быстрая сортировка")
data = load_from_file(list_of_data=[])
print(data)
print(quick_sort_opt(data))
