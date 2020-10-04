

s1 = "fairy tales"
s2 = "rail safety"

# Normalise strings
s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

# Checking if strings are equal
# Method requires log n time 
print(sorted(s1) == sorted(s2))

# Method 2 hash table/dic

def is_anagram(s1, s2):
    ht = dict()
    # If length is not equal it is not anagrom
    if len(s1) != len(s2):
        return False
    # Otherwise loop through both strings and keep track on what elements encountered
    for i in s1:
        if i in ht:
            # If element encountered more than onces
            ht[i] += 1
        else:
            # If first time encoutered
            ht[i] = 1

    # Substract matching elements
    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1

    # If anogram by checking for the remaining elements
    for i in ht:
        if ht[i] != 0:
            return False
    return True

print(is_anagram(s1, s2))

