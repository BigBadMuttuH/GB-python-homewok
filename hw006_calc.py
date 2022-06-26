# 1 Написать программу вычисления арифметического выражения заданного строкой.
# Используются операции +,-,/,*. приоритет операций стандартный.
# Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9;


# text = '2+2*5-8/2+3*1.5'
# text = '1+2*3'
# text = '1+3*4/2*9+10-2*2-1/0'


def parsing_elements(text: str) -> list:
    """
    parsing elements
    """
    enums = []
    numbers = ''
    for s in text:
        if s in '.0123456789':
            numbers += s
        elif s not in '0123456789' and numbers != '':
            enums.append(float(numbers))
            numbers = ''
        if s in '*/-+':
            enums.append(s)
        if s in '()':
            enums.append(s)
    if numbers != '':
        enums.append(float(numbers))
    # print(enums)
    return enums


def delete_elements(i, nlist, size):
    del nlist[i - 1]
    del nlist[i]
    i -= 1
    size = len(nlist)
    return i, size


def calculate(nlist: list):
    size = len(nlist)
    i = 1
    while 1 < size:
        while i < size:
            if type(nlist[i - 1]) == float and type(nlist[i + 1]) == float:
                if nlist[i] == '*':
                    nlist[i] = nlist[i - 1] * nlist[i + 1]
                    i, size = delete_elements(i, nlist, size)
                elif nlist[i] == '/':
                    try:
                        nlist[i] = nlist[i - 1] / nlist[i + 1]
                    except ZeroDivisionError:
                        print('нельзя делить на ноль')
                        exit()
                    i, size = delete_elements(i, nlist, size)
            i += 1
        i = 1
        while i < size:
            if type(nlist[i - 1]) == float and type(nlist[i + 1]) == float:
                if nlist[i] == '+':
                    nlist[i] = nlist[i - 1] + nlist[i + 1]
                    i, size = delete_elements(i, nlist, size)
                elif nlist[i] == '-':
                    nlist[i] = nlist[i - 1] - nlist[i + 1]
                    i, size = delete_elements(i, nlist, size)
            i += 1
        size = len(nlist)
        i = 1
    return nlist[0]


text = input("выражение без скобок: ")
nums = parsing_elements(text)
print(calculate(nums))
