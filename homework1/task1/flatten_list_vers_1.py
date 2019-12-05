def make_list_flatten(input_list, output_list):
    for i in input_list:
        if isinstance(i, list):
            make_list_flatten(i, output_list)
        else:
            output_list.append(i)
    return output_list


result = make_list_flatten([1, [2, 3], 4, [[6, 7]]], [])
print(result)
result = make_list_flatten([[4], 5, [[6, [7]]], [8], [[9, 10]]], [])
print(result)
