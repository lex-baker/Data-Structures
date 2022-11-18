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




## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


# My test cases

for n in range(10):
    arr = [i for i in range(random.randint(0, 48), random.randint(52, 100))]
    random.shuffle(arr)
    verified_answer = (min(arr), max(arr))
    my_answer = get_min_max(arr)
    print("Verified answer:", verified_answer, "and my answer:", my_answer)
    print ("Pass" if (verified_answer == my_answer) else "Fail")


print("\nEdge cases:\n")
# Edge cases
arr = [0]
print ("Pass" if ((0, 0) == get_min_max(arr)) else "Fail")

arr = [-2, 1]
print ("Pass" if ((-2, 1) == get_min_max(arr)) else "Fail")

arr = [1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 19, 0, 0]
print ("Pass" if ((0, 19) == get_min_max(arr)) else "Fail")