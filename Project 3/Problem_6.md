# Problem 6

To find the minimum and maximum of an unsorted array in a single traversal, I initialized two variables, 'max' and 'min', both set equal to the first value of the array. From there, I iterated over the array once, checking each value against 'max' first to see if it was the max, and if it wasn't, against 'min' to see if it was the min.


Time complexity: O(n), and in a single traversal of the array.

Space complexity: O(1)