# Problem 3

I first used a reverse merge sort to make sure all the digits are in order, then alternated adding the digits to the two numbers as I went down the array.

Time Complexity: O(  n * log(n) + n ) = O( n * (log(n) + 1) ) ~ O( n * (log(n)) ) = O( n * log(n) )
Space Complexity: O(n)