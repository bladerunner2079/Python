

data = [2,5,6,7,8,8,9]
target = 4

def find_closest_num(data, target):
    min_diff = float("inf")
    low = 0
    high = len(data) - 1
    closest_num = None

    # Edge case
    if len(data) == 0:
        return None
    if len(data) == 1:
        return data[0]

    while low <= high: 
        mid = (low + high) // 2
        # Ensure to not read beyond bounds of the list
        # Obtain left and right difference values
        if mid + 1 < len(data):
            min_diff_right = abs(data[mid+1] - target)
        if mid - 1 < len(data):
            min_diff_left = abs(data[mid-1] - target)

        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = data[mid-1]

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = data[mid+1]

        # Move mid-point accordingly
        if data[mid] < target:
            low = mid + 1
        elif data[mid] > target:
            high = mid - 1
        else:
            return data[mid]
    return closest_num 
        

print(find_closest_num(data, target))









