"""Count words in file."""

import sys
input_file = open(sys.argv[1])

def tokenize(in_file):
    my_list = []
    for line in in_file:
        for word in line.rstrip().split():
            my_list.append(word)
    return my_list

def count_words(list_of_word):
    word_dict = {}
    for word in list_of_word: 
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict

def print_dictionary(dict_):
    for key, value in dict_.items():
        print(f"{key} {value}")
    return

word_list = tokenize(input_file)
word_dict = count_words(word_list)
print_dictionary(word_dict)


