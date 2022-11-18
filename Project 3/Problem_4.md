# Problem 4

For Problem 4, the sorting algorithm used is a swapping sort. It iterates through the array and checks each value, and performs the following logic: If the number is 0, swap with the value at the saved index at the 'end' of the confirmed zeros, and increment that index. If the number is 2, swap with the value at the saved index at the 'beginning' of the confirmed twos, and decrement that index. 

Time complexity: O(n), but more importantly, there is only one traversal of the array.
Space complexity: O(1), because no new values were created besides a couple of index variables.