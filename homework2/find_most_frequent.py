import re


def find_most_frequent(text):
    modify_text = text.lower()
    list_of_input_words = re.findall(r'\w+', modify_text)
    words_dict = {}

    for word in list_of_input_words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

    most_frequent = 1
    most_frequent_word = []
    for key in words_dict:
        if words_dict[key] > most_frequent:
            most_frequent = words_dict[key]
            most_frequent_word = [key]
        elif words_dict[key] == most_frequent:
            most_frequent_word.append(key)

    most_frequent_word.sort()
    print(most_frequent_word)


find_most_frequent('Hello,Hello, my dear!')
find_most_frequent('to understand recursion you need first to understand recursion')
find_most_frequent('Mom! Mom! Are you sleeping?!!!')
find_most_frequent('my cat and I love fish my cat and I love fish my my cat my cat and I and and')

