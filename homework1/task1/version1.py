# make list flatten
# lst = [1, [2, 3], 4, [[6, 7]]]
# to
# lst = [1, 2, 3, 4, 6, 7]

# solution from: https://www.geeksforgeeks.org/python-convert-a-nested-list-into-a-flat-list/
# using recursion


input_list = [1, [2, 3], 4, [[6, 7]]]
output_list = []


def remove_nestings(input_lst):
    for i in input_lst:
        if isinstance(i, list):
            remove_nestings(i)
        else:
            output_list.append(i)


print('The original list: ', input_list)
remove_nestings(input_list)
print('The list after removing nesting: ', output_list)
