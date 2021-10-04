"""Count words in file."""

import sys

input_file = open(sys.argv[1])

# put your code here.
word_dict = {}
#lines = open(input_file)
for line in input_file:
    for word in line.rstrip().split():
        word_dict[word] = word_dict.get(word, 0) + 1
input_file.close()

for key, value in word_dict.items():
    print(f"{key} {value}")


