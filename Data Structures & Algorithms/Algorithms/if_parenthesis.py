# Import class
from stack_data import Stack

# Functions checks if paren match to each other
def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    # Index keeps track number of variables n the string
    index = 0

    # Loop continues while lenght of index is less then 0
    while index < len(paren_string) and is_balanced:
        # Checking first paren from the string
        paren = paren_string[index]
        if paren in "({[":
            # Pushes out paren
            s.push(paren)
        else:
            # Checks if the string is empty
            if s.is_empty():
                # If yes then its not balanced
                is_balanced = False
            else:
                # Pops second paren and checks if they match
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        # Increments per each string
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False


print(is_paren_balanced("()"))