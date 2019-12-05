def if_word_is_palindrome(input_text):
    modify_input_text = input_text.lower().replace(' ', '')
    reversed_text = modify_input_text[::-1]

    if modify_input_text == reversed_text:
        print('YES')
    else:
        print('NO')


if_word_is_palindrome('o12opo21o')
if_word_is_palindrome('0')
if_word_is_palindrome('puppy')
if_word_is_palindrome('mystring1Gni rts ym')
