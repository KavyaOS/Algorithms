def Merge(array, mid, left, right):
    num1 = mid - left + 1
    num2 = right - mid

    Left = [0] * num1
    Right = [0] * num2

    for i in range(0, num1):
        Left[i] = array[left + i]

    for j in range(0, num2):
        Right[j] = array[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < num1 and j < num2:
        if Left[i] <= Right[j]:
            array[k] = Left[i]
            i += 1
        else:
            array[k] = Right[j]
            j += 1
        k += 1

        while i < num1:
            array[k] = Left[i]
            k += 1
            i += 1

        while j<num2:
            array[k]=Right[j]
            k+= 1
            j+= 1


def MergeSort(array, left, right):
    if left < right:
        mid = (left + right - 1) // 2
        MergeSort(array, left, mid)
        MergeSort(array, mid + 1, right)
        Merge(array, mid, left, right)


array = [5, 3, 7, 2, 9]
print("Array before sorting:")
print(array)
n = len(array)
MergeSort(array, 0, n - 1)
print("Array after sorting:")
print(array)
