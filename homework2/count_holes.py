def count_holes(input_num):
    try:
        input_num = str(input_num).lstrip('0').lstrip('-')
        list_of_numbers = [int(x) for x in str(input_num)]
        sum_of_numbers = 0
        dict_of_numbers = {0: 1, 1: 0, 2: 0, 3: 0, 4: 1, 5: 0, 6: 1, 7: 0, 8: 2, 9: 1}

        for i in list_of_numbers:
            sum_of_numbers += dict_of_numbers[i]

        print(sum_of_numbers)

    except ValueError:
        print('ERROR')


count_holes('123')
count_holes(906)
count_holes('001')
count_holes(-8)
count_holes('-8.0')
count_holes('kkk')

