# ROT13
en_alphabet = "".join(
    list(map(chr, range(ord('A'), ord('Z') + 1)))
    + list(map(chr, range(ord('a'), ord('z'))))
)
# print(en_alphabet)
ru_alphabet = "".join(
    list(map(chr, range(ord('А'), ord('Я') + 1)))
    + list(map(chr, range(ord('а'), ord('я'))))
)
# print(ru_alphabet)


text = 'Тут какое-то сообщение'


def rot(string, alphabet, shift):
    """
    Шифрование со сдвигом.
    :param string: текст для (шифрования/расшифровки)
    :param alphabet: алфавит
    :param shift: сдвиг (дря расшифровки должен быть противоположным знаком)
    :return: зашифрованный/расшифрованный текст
    """
    result = ''
    for s in string:
        if s in alphabet:
            result += alphabet[(alphabet.find(s) + shift) % len(alphabet)]
        else:
            result += s

    return result


s1 = rot(text, ru_alphabet, 13)
print(s1)
s2 = rot(s1, ru_alphabet, -13)
print(s2)
