"""
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
Example:

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!

source: codewars.com
"""


def create_phone_number(n):
    n_str = "".join([str(i) for i in n])
    phone = "({}) {}-{}".format(n_str[0:3], n_str[3:6], n_str[6:10])
    return phone


no = [1,2,3,4,5,6,1,2,3,4]


print(create_phone_number(no))
