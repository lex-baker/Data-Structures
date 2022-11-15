# Problem 1

Seeing that 'expected time complexity is O(log(n))', I figured I should use a binary search algorithm. My process is to create an array of
every value from 0 to the number, inclusive, and then utilize a binary search to find the floor of the square root of the number given.

Given that each iteration of the binary search cuts the array in half, time complexity is O(log(n))
Space complexity is O(n), since an array with a length equaling the number given is created.