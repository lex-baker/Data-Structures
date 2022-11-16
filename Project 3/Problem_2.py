def find_rot_index(arr):
    # Finding the index where the originally sorted array would've started
    first = 0
    last = len(arr) - 1
    while len(arr[first:last+1]) > 2:
        mid = (last + first) // 2
        
        if arr[mid] < arr[first]:
            # Middle is less than first, rotational index is in first half of array
            last = mid
        elif arr[mid] > arr[last]:
            # Middle is greater than last, rotational index is in second half of array
            first = mid
        else:
            # Breakout to prevent endless loops in case provided array is not rotated
            return -1
    # During testing, it got down to the two elements where the rotation had happened, so the second one is the index wanted
    return last

def binary_search(arr, first, last, target):
    # Regular binary search    
    while first <= last:
        # Calculate midpoint
        mid = (first + last) // 2
        
        if target == arr[mid]:
            # If target is found
            return mid
        
        elif target < arr[mid]:
            # If target is smaller than midpoint, target is in first half of array
            last = mid - 1
        
        else:
            # If target is larger than midpoint, target is in second half of array
            first = mid + 1
    # Return -1 if target is not found
    return -1
    


# Template provided by Udacity
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    rot_index = find_rot_index(input_list)

    if input_list[len(input_list)-1] < number:
        # if the last element is smaller, the number being searched for is 
        # somewhere between 0 and rot_index
        return binary_search(input_list, 0, rot_index, number)
    else:
        # If it isn't, then the number is between rot_index and len(input_list) - 1
        return binary_search(input_list, rot_index, len(input_list) - 1, number)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[3, 4, 0, 1, 2], 4])
test_function([[3, 4, 0, 1, 2], 0])