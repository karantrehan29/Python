def binarySearch(arr, number):
    n = len(arr)
    low = 0
    high = n-1
    # Check if the array is not empty
    if n == 0:
        return -1
    # Start the while loop until low is less than or equal to high
    while low <= high :
        # Find the middle index of the array
        mid = (high + low) // 2
        # Check if the middle element is less than the target number
        if arr[mid]<number:
            # If so, update the low index to be one more than the middle index
            low = mid +1
        # Check if the middle element is greater than the target number
        elif arr[mid] > number:
            # If so, update the high index to be one less than the middle index
            high = mid - 1
        else:
            # If neither of the above conditions are met, the middle element is the target number
            return mid

    # If the target number is not found in the array, return -1
    return -1
