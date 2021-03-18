"""
Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string
with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased.
The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.
Each word should start with an uppercase.

The passed in string will only consist of alphabetical characters and spaces(' ').
Spaces will only be present if there are multiple words.
Words will be separated by a single space(' ').

Source: codewars.com
"""

def to_weird_case(string):
    new_characters = []
    n = 0

    for c in string:
        if c == " ":
            n = 0
            new_c = " "
        else:
            if n % 2 == 0:
                new_c = c.upper()
            else:
                new_c = c.lower()
            n += 1

        new_characters.append(new_c)

    new_string = ''.join(new_characters)

    return new_string


print(to_weird_case('ThIs Is A TeSt'))


# the highest rated solution:

def f1(word):
    return "".join([c.upper() if n % 2 == 0 else c for n, c in enumerate(word.lower())])


def f2(string):
    return " ".join([f1(word) for word in string.split()])

print(f2("Ciekawe czy zadziala"))