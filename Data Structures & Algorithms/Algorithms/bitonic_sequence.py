
data = [1,2,3,4,5,4,3,2,1]

def bitonic_sequence(data):
    low = 0
    high = len(data)-1

    # Bitonic sequence has to have at least 3 elements
    if len(data) < 3:
        return None

    while low <= high:
        mid = (low + high) // 2

        mid_left = data[mid - 1] if mid - 1 > 0 else float("-inf")
        mid_right = data[mid + 1] if mid + 1 < len(data)-1 else float("inf")

        if mid_left < data[mid] and mid_right > data[mid]:
            low = mid + 1
        elif mid_left > data[mid] and mid_right < data[data]:
            high = mid - 1
        elif mid_left < data[mid] and mid_right < data[mid]:
            return data[mid]




print(bitonic_sequence(data))


