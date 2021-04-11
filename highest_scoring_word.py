"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

source: codewars.com
"""

import string


LETTER_SCORES = dict((y, x) for x, y in enumerate(string.ascii_lowercase, 1))


def high(x):
    words = x.split()
    scores = []
    for word in words:
        score = 0
        for letter in word:
            if letter in LETTER_SCORES.keys():
                score += LETTER_SCORES[letter]
        scores.append(score)

    highest = words[scores.index(max(scores))]

    return highest


print(high("good morning everyone"))
