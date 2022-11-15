def find_rot_index(arr):
    # Finding the index where the originally sorted array would've started
    first = 0
    last = len(arr) - 1
    while len(arr[first:last+1]) > 2:
        mid = ((last - first) // 2) + first
        # print(first, mid, last, arr[first:last+1], len(arr[first:last+1]))
        
        if arr[mid] < arr[first]:
            # Middle is less than first, rotational index is in first half of array
            last = mid
        elif arr[mid] > arr[last]:
            # Middle is greater than last, rotational index is in second half of array
            first = mid
        else:
            # Breakout to prevent endless loops in case provided array is not rotated
            return -1
    # print(first, mid, last, arr[first:last+1], len(arr[first:last+1]))
    # During testing, it got down to the two elements where the rotation had happened, so the second one is the index wanted
    return last
    


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
    print("rot_index =", rot_index)


    first = rot_index
    local_last = rot_index - 1
    true_last = len(input_list) - 1
    while len(input_list[first:last+1]) > 2:
        mid = ((last - first) // 2) + first
        # print(first, mid, last, input_list[first:last+1], len(input_list[first:last+1]))
        
        if input_list[mid] < input_list[first]:
            # Middle is less than first, rotational index is in first half of array
            last = mid
        elif input_list[mid] > input_list[last]:
            # Middle is greater than last, rotational index is in second half of array
            first = mid
    # print(first, mid, last, input_list[first:last+1], len(input_list[first:last+1]))
    # During testing, it got down to the two elements where the rotation had happened, so the second one is the index wanted
    return last



    return index

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


print("rot_index =", find_rot_index([4, 0, 1, 2, 3]))

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([3, 4, 0, 1, 2], 4)
test_function([3, 4, 0, 1, 2], 0)