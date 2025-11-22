def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def print_array(arr):
    for element in arr:
        print(element, end=" ")
    print()

if __name__ == "__main__":
    my_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:")
    print_array(my_list)
    
    bubble_sort(my_list)
    
    print("Sorted array (Bubble Sort):")
    print_array(my_list)
