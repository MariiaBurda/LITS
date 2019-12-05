# count the number of holes


def count_holes(input_num):
    try:
        input_num = str(input_num)
        input_num = int(input_num)
        input_num = str(input_num).lstrip('0').lstrip('-')
        sum_of_numbers = 0
        dict_of_numbers = {'0': 1, '4': 1, '6': 1, '8': 2, '9': 1}

        for i in input_num:
            sum_of_numbers += dict_of_numbers.get(i, 0)

        print(sum_of_numbers)

    except ValueError:
        print('ERROR')


count_holes('123')
count_holes(906)
count_holes('001')
count_holes(-8)
count_holes(-8.0)
count_holes('kkk')

