def MERGE_SORT(arr, left, right):
    if left < right:
        mid = (left + right) // 2       
        MERGE_SORT(arr, left, mid)    
        MERGE_SORT(arr, mid + 1, right)
        MERGE(arr, left, mid, right)
