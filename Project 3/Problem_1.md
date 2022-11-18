# Problem 1

Seeing that 'expected time complexity is O(log(n))', I figured I should use a binary search algorithm. My process was originally to create an array of every number from 0 to the given number, but that was not very efficient. My second solution was to create the "frame" of an array, only actually using the midpoint and the left and right bounds of where the answer could be found. This new solution takes what actually was an O(n * log(n)) to the acceptable time complexity of O(log(n)), because each iteration of the binary search cuts the total amount of possible values in half.

Space complexity is O(1)