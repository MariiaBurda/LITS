# make list flatten
# lst = [1, [2, 3], 4, [[6, 7]]]
# to
# lst = [1, 2, 3, 4, 6, 7]

# solution from acquaintances

input_list = [1, [2, 3], 4, [[6, 7]]]


def flatten_array(input_lst):
    index = 0
    while index < len(input_lst):
        if type(input_lst[index]) != list:
            index += 1
            continue
        input_lst = input_lst[0:index] + input_lst[index] + input_lst[index + 1:]
    return input_lst


res = flatten_array(input_list)
print(res)
