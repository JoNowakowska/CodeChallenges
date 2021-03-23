"""
You will be given a vector of strings. You must sort it alphabetically
(case-sensitive, and based on the ASCII values of the chars) and then return the first value.

The returned value must be a string, and have "***" between each of its letters.

You should not remove or add elements from/to the array.

Source: codewars.com
"""


def two_sort(array):
    array.sort()
    el_of_interest = [i for i in array[0]]
    el_final = "***".join(el_of_interest)
    return el_final


print(two_sort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]))


# highest rate (min() returns the name with the lowest value, ordered alphabetically)
def two_sort(array):
    return '***'.join(min(array))