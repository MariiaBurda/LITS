string = '((((((((((((((2, 3)))))))))))))'


def balance_parenthesis(stri):
    sub1 = '('
    sub2 = ')'
    count1 = string.count(sub1)
    count2 = string.count(sub2)
    if count1 == count2:
        print('Parenthesis are balanced')
    else:
        print('Parenthesis are not balanced')


balance_parenthesis(string)


