### ДЗ № 1.
1. Сформировать список из  N членов последовательности.
```Для N = 5: 1, -3, 9, -27, 81 и т.д.```

2. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

3. Написать программу получающую набор произведений чисел от 1 до N.
```Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]```

4. Подсчитать сумму цифр в вещественном числе.

5. Написать функцию write_in_morse, которая принимает строку на английском языке и возвращает ее перевод на символьный язык Морзе. Ввод не должен зависеть от регистра. Да поможет вам этот словарь:
```python
char_to_dots = {
'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
'1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
'6': '-....', '7': '--...', '8': '---..', '9': '----.',
'&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
'-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}
```

[решение](https://github.com/BigBadMuttuH/GB-python-homewok/blob/main/hw001.py)

### ДЗ № 2.
1. Найти сумму чисел списка стоящих на нечетной позиции
```Пример:[1,2,3,4] -> 4```
2. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
```Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]```
3. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
```Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19```
4. Написать программу преобразования десятичного числа в двоичное.

[решение](https://github.com/BigBadMuttuH/GB-python-homewok/blob/main/hw002.py)

### ДЗ №3
1. Найти НОК двух чисел
2. Вычислить число Пи c заданной точностью d ```Пример: при d = 0.001,  c = 3.141.```
3. Составить список простых множителей натурального числа N
4. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
```Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]```

- на тему файловой системы:
5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 

[решение](https://github.com/BigBadMuttuH/GB-python-homewok/blob/main/hw003.py)

### ДЗ №4
Порядок элементов менять нельзя
1. Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию. 
2. Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие максимальное количество элементов.
```
Пример:
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
[5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
```
[решение сортировки](https://github.com/BigBadMuttuH/GB-python-homewok/blob/main/hw004_sorting.py)
[решение последовательности](https://github.com/BigBadMuttuH/GB-python-homewok/blob/main/hw004_sequence.py)

### ДЗ № 5
1. Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо. Используйте знания с последней лекции. Выполните ее в виде функции.
```
Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»
```
2. Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку.
3. Вот вам текст:
>«Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил».
Отфильтруйте его, чтобы этот текст можно было нормально прочесть. Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых.
5. Чисто для тренировки новый функций, ничего сложного. Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого плюс 1. Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами. Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков. Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы. С помощью reduce сложите получившиеся числа и верните из функции в качестве ответа.