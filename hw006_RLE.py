# реализовать RLE алгоритм

text = 'AABBBCCDDEEFFFGGGGFFJJJJJJFFFFFF'


def rle_encoding(data):
    result = ''
    prev_symbol = ''
    count = 1

    for s in data:
        if s != prev_symbol:
            if prev_symbol:
                result += str(count) + prev_symbol
            count = 1
            prev_symbol = s
        else:
            count += 1
    else:
        result += str(count) + prev_symbol
        return result


def rle_decoding(data):
    result = ''
    count = ''
    for s in data:
        if s.isdigit():
            count += s
        else:
            result += s * int(count)
            count = ''
    return result


encod = rle_encoding(text)
print(encod)
decode = rle_decoding(encod)
print(decode)
