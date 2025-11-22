def binarySearch(array, x, low, high):
  if high >= low:
    mid = low + (high - low) // 2

    if array[mid] == x:
      return mid

    if array[mid] > x:
      return binarySearch(array, x, low, mid - 1)

    return binarySearch(array, x, mid + 1, high)

  return -1
if __name__ == "__main__":
  arr = [2, 3, 4, 10, 40]
  x = 10
  result = binarySearch(arr, x, 0, len(arr)-1)

  if result != -1:
    print(f"Element {x} is present at index {result}")
  else:
    print(f"Element {x} is not present in array")
