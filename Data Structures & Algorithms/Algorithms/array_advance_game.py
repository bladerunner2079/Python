# Game rule - is it possible to advance to the end of the array by using array input?
# Each number represents the maximum you can advance in the array
# Example 1 array = [3,2,0,0,2,0,1] False
# Example 2 array = [3,3,1,0,2,0,1] True

# Solution
# Iterate through each entry in array by tracking furthest reachable element from current entry A[i] + i
# As + i is a array element number/value and A[i] is position in the array

def array_advanced(A):
    furthest_reached = 0
    last_idx = len(A) - 1
    i = 0
    while i <= furthest_reached and furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1
    return furthest_reached >= last_idx

A_1 = [3, 3, 1, 0, 2, 0, 1]
print(array_advanced(A_1))