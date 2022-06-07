import re
# 1. Напишите программу, удаляющую из текста все слова содержащие "абв",
# которое регистронезависимо.
# Используйте знания с последней лекции.
# Выполните ее в виде функции.
text = "стоп абвгдеж Вася пыво рабав копыто фабв Абкн абрыволк аБволк попыто"


def remove_abv(text):
    # result = ""
    # for t in text.split():
    #     if re.search(r"\b\w[^абв]\w+\b", t, re.IGNORECASE):
    #         result += t + " "
    # return result
    return "".join([t + " " for t in text.split() if re.search(r"\b\w[^абв]\w+\b", t, re.IGNORECASE)])

print(remove_abv(text))