def reverse_mergesort(arr):
    # Base case
    if len(arr) <= 1:
        return arr
    
    # Calculate the midpoint
    mid = len(arr) // 2

    # Split array in half
    left = arr[:mid]
    right = arr[mid:]
    
    # Continue recursively for both sides until every array only has one element, aka the base case
    left = reverse_mergesort(left)
    right = reverse_mergesort(right)
    
    # Finally, merge the arrays into a sorted form
    return merge(left, right)
    
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    # Compare and merge each element individually by walking down both arrays at the same time
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    # Add the final value(s) from whichever side still has values, which are already sorted
    merged += left[left_index:]
    merged += right[right_index:]
    
    return merged



def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    if len(input_list) < 2:
        return None

    # O(n * log(n)) worst-case
    input_list = reverse_mergesort(input_list)

    # I used strings to avoid having to multiply by increasing/decreasing orders of magnitude of 10.
    num1 = ""
    num2 = ""
    index = 0
    while index < len(input_list):
        num1 += str(input_list[index])
        if index + 1 < len(input_list):
            num2 += str(input_list[index + 1])
        index += 2
    # Convert the number strings to integers and return
    return [int(num1), int(num2)]
        


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])



# My tests
print("\nMy test and edge cases:\n")

test_function([[7, 2, 4, 0, 7], [740, 72]])
test_function([[1, 2], [2, 1]])
print("Pass" if (None == rearrange_digits([])) else "Fail") # rearrange_digits should return None if given array is less than two elements
test_function([[9, 9, 9, 9, 9, 9], [999, 999]])
test_function([[0, 0, 0, 0, 0, 0], [000, 000]])