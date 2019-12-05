def make_list_flatten(input_list):
    result_list = input_list[:]
    index = 0
    while index < len(result_list):
        if not isinstance(result_list[index], list):
            index += 1
            continue
        result_list = result_list[0:index] + result_list[index] + result_list[index + 1:]
    return result_list


res = make_list_flatten([1, [2, 3], 4, [[6, 7]]])
print(res)
result = make_list_flatten([[4], 5, [[6, [7]]], [8], [[9, 10]]])
print(result)
