# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append((i+1, next))

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                #print('mismatch opening one(beginning): ', i+1, next)
                return i+1

            if are_matching(opening_brackets_stack[-1][1], next):
                opening_brackets_stack.pop()
                #print('match one: ', i+1, next)
            else:
                #print('mismatch opening one: ', i+1, next)
                #print(are_matching(next, opening_brackets_stack[-1][1]))
                return i+1

    if len(opening_brackets_stack) != 0:
        #print('mismatch close one: ', opening_brackets_stack[-1][0], opening_brackets_stack[-1][1])
        return opening_brackets_stack[-1][0]
    
    return 0

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch == 0:
        print('Success')
    else:
        print(mismatch)

if __name__ == "__main__":
    main()
