# make list flatten
# lst = [1, [2, 3], 4, [[6, 7]]]
# to
# lst = [1, 2, 3, 4, 6, 7]

# solution from acquaintances

input_list = [1, [2, 3], 4, [[6, 7]]]


def flatten_array(input_lst):
    result_lst = input_lst[:]
    index = 0
    while index < len(result_lst):
        if type(result_lst[index]) != list:
            index += 1
            continue
        result_lst = result_lst[0:index] + result_lst[index] + result_lst[index + 1:]
    return result_lst


res = flatten_array(input_list)
print(res)
