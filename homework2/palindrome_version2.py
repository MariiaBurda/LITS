def if_word_is_palindrome(input_text):
    modify_input_text = input_text.lower().replace(' ', '')
    result = 'YES'
    index = 1
    for i in range(len(modify_input_text) // 2):
        if modify_input_text[index-1] == modify_input_text[-index]:
            index += 1
        else:
            result = 'NO'
            break
    print(result)


if_word_is_palindrome('o12opo21o')
if_word_is_palindrome('0')
if_word_is_palindrome('puppy')
if_word_is_palindrome('mystring1Gni rts ym')
