def binary_search(arr, low, high, key):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, low, mid-1, key)
        else:
            return binary_search(arr, mid+1, high, key)
    else:
        return -1

arr = [1, 2, 3, 4, 5, 10]
key = 10
j = binary_search(arr, 0, len(arr)-1, key)
print("Element found at index:", str(j))