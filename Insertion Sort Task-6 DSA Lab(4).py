def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def print_array(arr):
    for element in arr:
        print(element, end=" ")
    print()


if __name__ == "__main__":
    my_list = [12, 11, 13, 5, 6]
    print("Original array:")
    print_array(my_list)
    
    insertion_sort(my_list)
    
    print("Sorted array (Insertion Sort):")
    print_array(my_list)
