"""
4. Чисто для тренировки новых функций, ничего сложного.
Создайте два списка — один с названиями языков программирования,
другой — с числами от 1 до длины первого плюс 1.
Вам нужно сделать две функции:
первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
Вторая — которая отфильтрует этот список следующим образом:
    если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже,
    то кортеж остается, его номер заменяется на сумму очков.
    Если нет — удаляется.
    Суммой очков называется сложение порядковых номеров букв в слове.
    Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
    Это — 16ричная система, поищите, как правильнее и быстрее получать эти символы.
    С помощью reduce сложите получившиеся числа и верните из функции в качестве ответа.
"""
from functools import reduce

prog_lang = [
    'Fortran',
    'Cobol',
    'Pascal',
    'C',
    'Depth',
    'Assembler',
    'Python',
    'Go',
    'Java',
    'Rust',
    'Algol',
    'Basic',
    'LISP'
]


def get_list_of_tuples(data):
    return list(zip([i for i in range(1, len(data) + 1)], data))


def get_sums(data, result=[]):
    for key, value in data:
        word_cost = reduce(lambda s, v:
                           s + ord(v) - ord('@'),
                           value.upper(), 0)
        # print(f"{key=}, {value=}, {word_cost=}")
        if word_cost % key == 0:
            # print(f"!!!!!{key=}, {value=}")
            result += [(word_cost, value)]
    return result

num_lang = get_list_of_tuples(prog_lang)
print(num_lang)

print(get_sums(num_lang))