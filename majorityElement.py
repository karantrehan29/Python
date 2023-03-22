def majority_element(arr):
    # check if the array is empty
    if not arr:
        return None

    # initialize the count and candidate element
    count = 1
    candidate = arr[0]

    # find the candidate element using the Boyer-Moore voting algorithm
    for i in range(1, len(arr)):
        if arr[i] == candidate:
            count += 1
        else:
            count -= 1
            if count == 0:
                candidate = arr[i]
                count = 1

    # count the occurrences of the candidate element in the array
    count = sum(1 for elem in arr if elem == candidate)

    # return the majority element if it exists
    if count > len(arr) // 2:
        return candidate
    else:
        return None
