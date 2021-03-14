"""
Introduction

There is a war and nobody knows - the alphabet war!
There are two groups of hostile letters.
The tension between left side letters and right side letters was too high and the war began.

Task
Write a function that accepts fight string consists of only small letters
and return who wins the fight. When the left side wins return Left side wins!,
when the right side wins return Right side wins!,
in other case return Let's fight again!.
"""


def alphabet_war(fight):
    # defining initial scores and a winner
    left_score = 0
    right_score = 0
    winner = ''

    # defining weapons of both teams
    left_weapons = {
        "w": 4,
        "p": 3,
        "b": 2,
        "s": 1
    }
    right_weapons = {
        "m": 4,
        "q": 3,
        "d": 2,
        "z": 1
    }

    # fight
    for f in fight:
        if f in left_weapons:
            left_score += left_weapons[f]
        elif f in right_weapons:
            right_score += right_weapons[f]

    # checking who won
    if left_score > right_score:
        winner = 'Left side wins!'
    elif left_score < right_score:
        winner = 'Right side wins!'
    else:
        winner = 'Let\'s fight again!'

    return winner
