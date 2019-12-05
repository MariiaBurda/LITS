import re


def find_most_frequent(input_text):
    modify_text = input_text.lower()
    list_of_input_words = re.findall(r'\w+', modify_text)
    set_of_words = set(list_of_input_words)
    res = {}
    for unique_word in set_of_words:
        res.setdefault(list_of_input_words.count(unique_word), []).append(unique_word)

    print(res[max(res)])


find_most_frequent('Hello,Hello, my dear!')
find_most_frequent('to understand recursion you need first to understand recursion')
find_most_frequent('Mom! Mom! Are you sleeping?!!!')
find_most_frequent('my cat and I love fish my cat and I love fish my my cat my cat and I and and')
