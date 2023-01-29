def binarySearch(arr, number):
    n = len(arr)
    low = 0
    high = n-1

    while low <= high :
        mid = (high + low) // 2
        if arr[mid]<number:
            low = mid +1

        elif arr[mid] > number:
            high = mid - 1
        else:
            return mid

    return -1


