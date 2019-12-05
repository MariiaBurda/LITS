# module for converting a number from any number system to any (up to 36)
# we use function convert_n_to_m (x, n, m)
# function convert number x from n-number system to m-number system

import re


def val(c):
    if c >= '0' and c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10


def to_deci(input_str, from_base):
    llen = len(input_str)
    power = 1
    input_num_in_decimal = 0

    for i in range(llen - 1, -1, -1):
        if val(input_str[i]) >= from_base:
            return False
        input_num_in_decimal += val(input_str[i]) * power
        power *= from_base
    if input_num_in_decimal < 0:
        return False
    return input_num_in_decimal


def re_val(num):
    if num >= 0 and num <= 9:
        return chr(num + ord('0'))
    else:
        return chr(num - 10 + ord('A'))


def from_deci(to_base, input_num_in_decimal):
    res = ''
    if not input_num_in_decimal:
        return False
    else:
        while input_num_in_decimal > 0:
            res += re_val(input_num_in_decimal % to_base)
            input_num_in_decimal = int(input_num_in_decimal / to_base)

        res = res[::-1]
        return res


def check_x_instance(x):
    try:
        x = str(x)
        result = re.findall(r'^\w+$', x)
        return result[0]
    except:
        return 'False'


def convert_n_to_m(x, n, m):
    checking_res = check_x_instance(x)
    if checking_res == 'False':
        print(checking_res)
    elif 1 <= n and m == 1:
        res = '0' * to_deci(str(x), n)
        print(res)
    elif 1 <= n and m <= 36:
        res = from_deci(m, to_deci((str(x)), n))
        print(res)
    else:
        print('False')


convert_n_to_m([123], 4, 3)
convert_n_to_m('0123', 5, 6)
convert_n_to_m('123', 3, 5)
convert_n_to_m(123, 4, 1)
convert_n_to_m(-123.0, 11, 16)
convert_n_to_m('A1Z', 36, 16)
convert_n_to_m('-123', 4, 3)
