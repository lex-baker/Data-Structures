def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # Overall index
    index = 0
    # Index of end of zeros
    index_0 = 0
    # Index of beginning of twos
    index_2 = len(input_list) - 1
    
    while index <= index_2:
    # Continue until regular index reaches the beginning of the twos
        if input_list[index] == 0:
            # If the element is 0, swap with the next value after the zeros
            input_list[index] = input_list[index_0]
            input_list[index_0] = 0
            index_0 += 1
            index += 1
        elif input_list[index] == 2:
            # If element is 2, swap with value at beginning of twos
            input_list[index] = input_list[index_2] 
            input_list[index_2] = 2
            index_2 -= 1
        else:
            # If element equals 1, just increment the index
            index += 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# My tests
print("\nMy Test and edge cases:\n")
test_function([2, 1, 0])
test_function([0])
test_function([])
test_function([0, 0, 0])