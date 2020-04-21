#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#
import re


def reverse_words_order_and_swap_cases(sentence):
    sentence = re.split(r" ", sentence)
    sentence = ["".join([letter.swapcase() for letter in word])
                for word in sentence]
    sentence.reverse()
    sentence = " ".join(sentence)
    return sentence


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
