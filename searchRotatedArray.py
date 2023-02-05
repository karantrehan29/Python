def searchRotatedArray(nums,target):

    # Length of the array
    len_arr = len(nums)

    # if array is empty return -1
    if  0 == len_arr:
        return -1

    low = 0
    high = len_arr - 1

    # modified binary search
    while low<=high:
        mid = (low + high)//2
        if target == nums[mid]:
            return mid

        # If left part of array from mid is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # If right part of array from mid is sorted
        elif nums[mid] <= nums[high]:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

