"""
Find the sum of the digits of all the numbers from 1 to N (both ends included).
Examples

# N = 4
1 + 2 + 3 + 4 = 10

# N = 10
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) = 46

# N = 12
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) + (1 + 1) + (1 + 2) = 51

source: codewars.com
"""

def compute_sum(n):
    list_of_digits = []
    for i in range(1, n+1):
        str_i = str(i)
        if len(str_i) == 1:
            list_of_digits.append(i)
        elif len(str_i) > 1:
            sublist = [int(j) for j in str_i]
            list_of_digits += sublist
    sum_n_digits = sum(list_of_digits)

    return sum_n_digits


print(compute_sum(12))

# oneliner by acu192:
def compute_sum(n):
    return sum(int(c) for i in range(1, n+1) for c in str(i))