def bin_search(num, arr):
    # Repeat until only one value remains in the array
    while len(arr) > 1:
        # Calculate the middle_index
        middle_index = (len(arr) - 1) // 2
        
        # Finding the middle element
        middle = arr[middle_index]
        # Calculating the square to avoid unneccessary calculations in the if-elif-else statement
        squared = middle * middle
        
        if squared == num:
            # The square root was found exactly
            return middle
        
        elif squared > num:
            # Square root is in the smaller half of the array
            return bin_search(num, arr[0:middle_index])
        
        else:
            # Square root is in the bigger half of the array
            return bin_search(num, arr[middle_index+1:len(arr)])
    # If this return statement is reached, it means there is only one value in the array, which is therefore the square root     
    return arr[0]


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # Create an array of [0, 1, 2...n-2, n-1, n]
    allVals = list(range(number+1))
    # Call to the recursive binary search
    return bin_search(number, allVals)

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")