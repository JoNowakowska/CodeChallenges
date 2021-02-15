"""
The goal of this exercise is to convert a string to a new string where each character in the new string
is "(" if that character appears only once in the original string,
or ")" if that character appears more than once in the original string.
Ignore capitalization when determining if a character is a duplicate.
"""


word = 'din'


def duplicate_encode(word):
    word = word.lower()
    d = dict()
    encoded_word = []
    for x in word:
        if x in d:
            d[x] = d[x] + 1
        else:
            d[x] = 1

    for x in word:
        if d[x] == 1:
            encoded_word.append('(')
        elif d[x] > 1:
            encoded_word.append(')')

    return ''.join(encoded_word)


print(duplicate_encode(word))