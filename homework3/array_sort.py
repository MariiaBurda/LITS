# function for array sorting (bubble sort method)


def bubble_sort(array, reverse=False):
    # go through all elements
    for i in range(len(array) - 1):
        elements_are_swapped = False
        # elements are not swapped yet in this iteration
        for j in range(0, len(array)-i-1):
            # go through elements from index 0 to len(array)-i-1
            # if found element is larger than next, swap them
            if not reverse:
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    elements_are_swapped = True
            else:
                if array[j] < array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    elements_are_swapped = True

        # if there are no swapped pairs in the iteration, then the array is sorted
        if not elements_are_swapped:
            break
    return array


sorted_array = bubble_sort([8, 2, 1, 7, -1, 0.5])
print('Sorted list: ', sorted_array)
reversed_array = bubble_sort([8, 2, 1, 7, -1, 0.5], reverse=True)
print('Reversed array', reversed_array)
