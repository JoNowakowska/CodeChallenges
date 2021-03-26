"""
Given a string str, reverse it omitting all non-alphabetic characters.
Example

For str = "krishan", the output should be "nahsirk".

For str = "ultr53o?n", the output should be "nortlu".
Input/Output

    [input] string str

    A string consists of lowercase latin letters, digits and symbols.

    [output] a string

source: codewars.com
"""


def reverse_letter(string):
    ALPHABET = 'abcdefghijklmnoqprstuvwxyz'

    str_len = len(string)
    new_order = []

    for i in range(str_len-1, -1, -1):
        char = string[i]
        if char in ALPHABET:
            new_order.append(char)

    new_str = ''.join(new_order)

    return new_str


print(reverse_letter("krishan"))


# other cool solutions:
def reverse_letter(s):
  return ''.join([i for i in s if i.isalpha()])[::-1]

def reverse_letter(string):
    return ''.join(c for c in string[::-1] if c.isalpha())

def reverse_letter(string):
    return ''.join(filter(str.isalpha, reversed(string)))

import re
def reverse_letter(string):
    return re.sub("[^a-zA-Z]","",string)[::-1]
