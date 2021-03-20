"""
Given an array of positive or negative integers

I= [i1,..,in]

you have to produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers.
The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.

Example:

I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]

[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

Notes:

    It can happen that a sum is 0 if some numbers are negative!

Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers
for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.

    In Fortran - as in any other language - the returned string is not permitted to contain
    any redundant trailing whitespace: you can use dynamically allocated character strings.

source: codewars.com
"""

from math import ceil, sqrt


def detect_prime_factors(max_value):
    """Check all the integers up to a max_value and add to a set if primes. Return the prime_factors set."""
    prime_factors = set()

    for i in range(2, max_value + 1):
        if i == 2 or i == 3 or i == 5:  # add 2, 3, 5 to the prime_factors set
            prime_factors.add(i)
        elif i > 5:
            if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:  # pass on 'i' if it is clearly not a prime
                pass
            else:  # check further if 'i' is a prime
                for el in range(2, ceil(sqrt(i)) + 1):
                    if i % el == 0:  # move to the next element if it eventually is not a prime
                        break
                    else:  # add the prime to the prime_factors set
                        prime_factors.add(i)

    return sorted(prime_factors)


def sum_for_list(lst):
    """Look for prime factors' dividends, sum them, append a prime factor and the sum to the list. Return final list"""

    abs_lst_sort = sorted([abs(el) for el in lst])
    max_value = abs_lst_sort[-1]

    prime_factors = detect_prime_factors(max_value)

    final_list = []
    for i in prime_factors:
        sums = 0
        to_append = False
        for el in lst:
            if abs(el) >= i:  # if a lst element can be divided by a prime factor, add its value to sums
                if el % i == 0:
                    sums += el
                    to_append = True
        if to_append:  # if one/more lst elements are dividends, add the prime and their sum to the final_list
            final_list.append([i, sums])

        to_append = False

    return final_list


print(sum_for_list([15, 21, 24, 30, 45, 1, 2, 3, 37, 223]))


# the solution is too slow to pass. Don't have an access to other solutions.
