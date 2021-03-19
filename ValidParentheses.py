"""
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and false if it's invalid.
Examples

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Constraints

0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters.
Furthermore, the input string may be empty and/or not contain any parentheses at all.
Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).

Source: codewars.com
"""


def valid_parentheses(string):
    count_open = 0
    count_close = 0
    for i in string:
        if i == "(":
            count_open += 1
        elif i == ")":
            count_close += 1
        if count_open < count_close:
            return False
    if count_open != count_close:
        return False
    elif count_open == count_close:
        return True


print(valid_parentheses("())"))


# clever solution by albarralnunez:
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False