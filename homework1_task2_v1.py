# check if parenthesis are balanced


def check_if_parenthesis_are_balanced(input_str):
    open_sign = '('
    close_sign = ')'
    count_open_signs = input_str.count(open_sign)
    count_close_signs = input_str.count(close_sign)
    if count_open_signs == count_close_signs:
        print('Parenthesis are balanced')
    else:
        print('Parenthesis are not balanced')


input_string = '((((((((((((((2, 3)))))))))))))'
check_if_parenthesis_are_balanced(input_string)
