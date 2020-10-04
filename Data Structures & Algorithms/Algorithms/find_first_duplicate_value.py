

data = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
target = 108

# Linear Method
def find_first_dup_element_linear(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i 

def find_first_dup_element(data, target):
    low = 0
    high = len(data)-1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] < target:
            low = mid + 1
        if data[mid] > target:
            high = mid - 1
        else:
            if data[mid] != target:
                return mid

         
