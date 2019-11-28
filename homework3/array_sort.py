# function for array sorting (bubble sort method)


def bubble_sort(array):
    # go through all elements
    for i in range(len(array) - 1):
        elements_are_swapped = False
        # elements are not swapped yet in this iteration
        for j in range(0, len(array)-i-1):
            # go through elements from index 0 to len(array)-i-1
            # if found element is larger than next, swap them
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                elements_are_swapped = True
        # if there are no swapped pairs in the iteration, then the array is sorted
        if not elements_are_swapped:
            break
    print('Sorted list: ', array)
    return array


def reversed_array(array):
    for i in range(len(array) - 1):
        elements_are_exchanged = False
        for j in range(0, len(array) - i - 1):
            # go through elements from index 0 to len(array)-i-1
            # if found element is smaller than next, swap them
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                elements_are_exchanged = True
        if not elements_are_exchanged:
            break
    print('Reversed_list: ', array)


sorted_list = bubble_sort([8, 2, 1, 7, -1, 0.5])
reversed_array(sorted_list)
