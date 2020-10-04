

data = [-10, -5, 0, 3, 7]

# Time complexity 0(n)
# Space complexity 0(1)
def find_fixed_point_lienar(data):
    for i in range(len(data)):
        if data[i] == i:
            return data[i]
    return None

# Time Complexity: O(log n)
# Space Complexity: O(1)
def find_fixed_point(data):
    low = 0 
    high = len(data)-1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] < mid:
            low = mid + 1
        elif data[mid] > mid:
            high = mid - 1
        else:
            return data[mid]
    return False

    
print(find_fixed_point(data))













