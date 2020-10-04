A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

# General solution 
print(set(A).intersection(B))

# Method 2 uses two points at the beginning of each list and compares first element values,
# If first list value is not equal it will move the the second element
# and comapre against second list first element value
def intersect_sorted_array(A, B):
    i = 0
    j = 0
    intersection = []

    while i < len(A) and j < len(B): 
        if A[i] == B[j]:
            if A[i]  != A[i-1]:
                intersection.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1 
    return intersection


print(intersect_sorted_array(A, B))

