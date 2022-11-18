# Problem 3

I first used a reverse merge sort to make sure all the digits are in order, then alternated adding the digits to the two numbers as I went down the array. I choose a merge sort because it is one of the few sorting algorithms that can operate in worst-case O(n * log(n)) time, and I understand it better than other possiblities. The merge sort algorithm is of the divide-and-conquer variety, so it breaks the array into its smallest parts, then builds it back up again in a correct order.

Time Complexity: O(  n * log(n) + n ) = O( n * (log(n) + 1) ) ~ O( n * (log(n)) ) = O( n * log(n) )
Space Complexity: O(n)