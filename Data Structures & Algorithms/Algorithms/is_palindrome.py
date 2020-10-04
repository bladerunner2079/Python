
s = "Was it a cat I saw"

# Linear space solution 
s = "".join([i for i in s if i.isalpha()]).replace(" ", "").lower()

# Check if palendrome
print(s == s[::-1])
print(s)

# Method 2
def is_palindrome(s):
    # Two points are set at both ends of string which will compare elements  
    i = 0
    j = len(s) - 1

    while i < j:
        # Loop checks if element is alpha numeric and less then j and continue to compare elements
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j]. isalnum() and i < j:
            j -= 1
        # Checks if elements in lower case are equal
        if s[i].lower() != s[j].lower():
            return False

        # Keep moving through the list
        i += 1
        j -= 1
    return True

print(is_palindrome(s))
