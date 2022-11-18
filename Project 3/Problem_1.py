# Template provided by Udacity
def bin_search(num, lower, upper):
    # Running a binary search without an array
    
    # Calculate midpoint between range
    current = (upper + lower) // 2
    # Calculating the square to avoid unneccessary calculations in the if-elif-else statement
    squared = current**2
    if squared == num:
        # The square root was found exactly
        return current
    
    elif squared < num:
        # Square root is in the bigger half of the array
        # Before running another search, make sure the next value up isn't over our goal (indicates the current value should be returned)
        if (current + 1)**2 > num:
            # If the next number up, squared, is bigger, then the floored square of the number should be the number we have now.
            return current
        else:
            return bin_search(num, current + 1, upper)
    
    else:
        # Square root is in the smaller half of the array
        return bin_search(num, lower, current)


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # Check that value isn't negative
    if number < 0:
        return None
    # Call to the recursive binary search, providing the middle value
    return bin_search(number, 0, number)

print ("Pass for 9" if  (3 == sqrt(9)) else "Fail")
print ("Pass for 0" if  (0 == sqrt(0)) else "Fail")
print ("Pass for 16" if  (4 == sqrt(16)) else "Fail")
print ("Pass for 1" if  (1 == sqrt(1)) else "Fail")
print ("Pass for 27" if  (5 == sqrt(27)) else "Fail")

# My own test cases

# Test every number from 0 to 100
for n in range(101):
    square_root = int(n**(1/2))
    # print(square_root) # Testing
    print ("Pass for " + str(n) if  (square_root == sqrt(n)) else "Fail for " + str(n))

# Test very high number
print ("Pass for 94673825" if  (9730 == sqrt(94673825)) else "Fail")

# Test negative number
print ("Pass for -1" if  (None == sqrt(-1)) else "Fail")