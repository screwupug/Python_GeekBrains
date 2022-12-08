# ======================================================================================
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# ======================================================================================
data = "AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE"


def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data:
        return ''
    for char in data:
        if char == prev_char:
            count += 1
        else:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
    encoding += str(count) + prev_char
    return encoding

def rle_decoding(data):
    decode = ''
    count = ''

    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


a = rle_encode(data)
b = rle_decoding(a)
print(a)
print(b)
