def searchRotatedArray(arr,element):

    # Length of the array
    len_arr = len(arr)

    # if array is empty return -1
    if  0 == len_arr:
        return -1

    low = 0
    high = len_arr - 1

    # modified binary search
    while low<=high:
        mid = (low + high)//2
        if element == arr[mid]:
            return mid

        # If left part of array from mid is sorted
        if arr[low] <= arr[mid]:
            if arr[low] < element < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # If right part of array from mid is sorted
        elif arr[mid] <= arr[high]:
            if arr[mid] < element < arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1



