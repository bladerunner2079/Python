


data = [1,2,3,4,5,6,7]

def find(data):
    low = 0
    high = len(data) - 1
    
    while low < high:
        mid = (low + high) // 2
 
        if data[mid] > data[high]:
            low = mid + 1
        elif data[mid] <= data[high]:
            high = mid

    return low

idx = find(data)
print(data[idx])




