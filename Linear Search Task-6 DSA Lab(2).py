def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

my_list = [4, 2, 7, 1, 9, 5]
target_element = 7
result = linear_search(my_list, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}")
else:
    print(f"Element {target_element} not found in the list")

target_element_not_found = 3
result_not_found = linear_search(my_list, target_element_not_found)

if result_not_found != -1:
    print(f"Element {target_element_not_found} found at index {result_not_found}")
else:
    print(f"Element {target_element_not_found} not found in the list")
