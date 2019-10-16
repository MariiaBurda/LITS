# check if parenthesis are balanced
# str = '((((((((((((((2, 3)))))))))))))'
# solution from https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/
# this solution for more complicated cases

open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


# Function to check parentheses
def check_if_parenthesis_are_balanced(input_str):
    stack = []
    for i in input_str:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Unbalanced"
        else:
            continue
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


input_string = "((((((((((((((2, 3)))))))))))))"
print(input_string, "-", check_if_parenthesis_are_balanced(input_string))

# more complicated cases
# input_string = "{[]{()}}"
# input_string = "[{}{})(]"
