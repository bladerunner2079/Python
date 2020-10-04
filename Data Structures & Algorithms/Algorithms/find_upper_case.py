

input_strin_1 = "machineLearning"
input_strin_2 = "MachineLearning"
input_strin_3 = "machinelearning"

def find_upper_case_iterative(input_string):
    for i in range(len(input_string)):
        if input_string[i].isupper():
            return input_string[i]
    return "No upper case found"

# print(find_upper_case_iterative(input_strin_1))
# print(find_upper_case_iterative(input_strin_2))
# print(find_upper_case_iterative(input_strin_3))


def find_upper_case_recursive(input_string, idx=0):
    if input_string[idx].isupper():
        return input_string[idx]
    if idx == len(input_string) - 1:
        return "No upper case element found"
    return find_upper_case_recursive(input_string, idx + 1)

print(find_upper_case_recursive(input_strin_1))
print(find_upper_case_recursive(input_strin_2))
print(find_upper_case_recursive(input_strin_3))

