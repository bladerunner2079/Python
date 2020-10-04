

# Given - An array of non-negative digits that represent a decimal integer
# Problem - Add one to the integer.
# Assume the solution still works even if implemented in a language with finite-precision arithmetic.

# Example
# array = 149
# +1
# array = 150

A = [1, 4, 9]
A_1 = [9, 9, 9]

# One-line solution is to smash all elements to string and convert it back to int (cheeky solution!)
add_number = 1
s = "".join(map(str, A))
print(int(s) + 1)

# Master slam solution
def plus_one(A):
    # Index last element of the array and add given number
    A[-1] += 1
    # Loop in reverse order of the array
    for i reversed(range(1, len(A))):
        # Checking if it is not equal to 10 and do not have 1 carry/memory
        if A[i] != 10:
            break
        # Otherwise keep current element 0 and add carry to the next i-1 element
        A[i] = 0
        A[i-1] += 1
    # Checking if first element is equal to 10, add zero to the end of array and remove zero from the first element
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

print(plus_one(A))