def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
        ints(list): list of integers containing one or more integers
    """
    max = ints[0]
    min = ints[0]
    # Skip the first since that's an unnecessary calculation
    # Finding max and min in a single traversal
    for n in ints[1:]:
        if n > max:
            max = n
        elif n < min:
            min = n

    return (min, max)

def initial_o_n_time_sort(arr):
    # This sorting alogrithm is pretty specific (to integers within a range of 0 to (length of array - 1)) and not very space efficient
    arr_length = len(arr) 
    sorted_arr = []

    # Create an array of None to the size of the unsorted array
    for l in range(arr_length):
        sorted_arr.append(None)
    
    # Move the values in the original array to their value's index place
    for n in arr:
        sorted_arr[n] = n

    print(sorted_arr)
    return sorted_arr

def improved_o_n_time_sort(arr):
    # This sorting alogrithm is slightly more versatile but even less space efficient
    # Duplicate values will not be preserved
    min, max = get_min_max(arr)
    arr_length = (max - min) + 1
    intermediate_arr = []

    # Create an array of None to the size of the largest value in the array minus the smallest value
    for l in range(arr_length):
        intermediate_arr.append(None)
    
    # Move the values in the original array to their value's index place, which potentially leaves many None's behind
    for n in arr:
        intermediate_arr[n - min] = n

    # Now, instead of removing values when they equal None, which has potential worst case time complexity of O(n), we make a third array
    # Overall, that has a time complexity of O(n), and skips over value that equal None
    sorted_arr = []

    for n in intermediate_arr:
        if n:
            sorted_arr += [ n ]


    print(sorted_arr)
    return sorted_arr

def final_o_n_time_sort(arr):
    # This avoids detroying duplicate values, but has worst case time complexity of O(n) ????
    min, max = get_min_max(arr)
    arr_length = (max - min) + 1
    intermediate_arr = []

    for l in range(arr_length):
        intermediate_arr.append(None)
    
    # In this algorithm, every duplicate value increments a counter (originally, it was an array of duplicated values, but that is neither
    # space nor time efficient)
    for n in arr:
        if intermediate_arr[n - min] is None:
            intermediate_arr[n - min] = [ n, 1 ]
        else:
            intermediate_arr[n - min][1] += 1

    # Now, instead of removing values when they equal None, which has potential worst case time complexity of O(n), we make a third array
    # Which overall has time complexity of O(n)
    sorted_arr = []

    for n in intermediate_arr:
        if n:
            for v in range(n[1]):
                sorted_arr += [ n[0] ]

    print(sorted_arr)
    return sorted_arr

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

# More testing
test_array = [5, 2, 2, 9, 3, 6]

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9] == initial_o_n_time_sort(l)) else "Fail")
print ("Pass" if ([2, 3, 5, 6, 9] == improved_o_n_time_sort(test_array)) else "Fail") # Ignores duplicates
print ("Pass" if ([2, 2, 3, 5, 6, 9] == final_o_n_time_sort(test_array)) else "Fail") # Considers duplicates