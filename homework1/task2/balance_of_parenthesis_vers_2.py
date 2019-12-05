def check_if_parenthesis_are_balanced(input_str):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]

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

input_string = "{[]{()}}"
print(input_string, "-", check_if_parenthesis_are_balanced(input_string))

input_string = "[{}{})(]"
print(input_string, "-", check_if_parenthesis_are_balanced(input_string))

input_string = "[{}]{}[]"
print(input_string, "-", check_if_parenthesis_are_balanced(input_string))
