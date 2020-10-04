
s1 = "Tact Coa"
s2 = "This is not a palindrome permutation"

def is_palem_perm(input_str):
    input_str = input_str.replace(" ", "").lower()
    d = dict()

    # Loop through the elements and ask if they are in the dict
    for i in input_str:
        if i in d:
            # If value already exist in dict, increment cout of it by one
            d[i] += 1
        else:
            # Add new element to the dict
            d[i] = 1

    odd_count = 0
    for k, v in d.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True

print(is_palem_perm(s1))
print(is_palem_perm(s2))
