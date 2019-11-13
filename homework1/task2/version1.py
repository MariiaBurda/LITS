# check if parenthesis are balanced
# my solution using functions


def check_if_parenthesis_are_balanced(input_str):
    count_open_signs = 0
    count_close_signs = 0
    result = 'Parentheses are balanced'
    for symbol in input_str:
        if symbol == '(':
            count_open_signs += 1
            continue
        elif symbol == ')':
            count_close_signs += 1
            if count_close_signs <= count_open_signs:
                continue
            else:
                result = 'Parentheses are not balanced'
                break
        else:
            continue
    if count_open_signs == 0 and count_close_signs == 0:
        result = "This string doesn't have parentheses"
    print(result)


check_if_parenthesis_are_balanced('((2, 3))')
check_if_parenthesis_are_balanced(')))1+1(((')
check_if_parenthesis_are_balanced('ps')



