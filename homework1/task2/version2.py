# check if parenthesis are balanced
# str = '((((((((((((((2, 3)))))))))))))'
# solution from https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/

open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


# Function to check parentheses
def check(myStr):
    stack = []
    for i in myStr:
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


# Driver code
#string = "{[]{()}}"
#print(string, "-", check(string))

#string = "[{}{})(]"
#print(string, "-", check(string))

string = "((((((((((((((2, 3)))))))))))))"
print(string, "-", check(string))


