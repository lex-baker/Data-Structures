# Problem 2

I used two binary searches, the first of which found the "rotational index" or which index of the rotated array would've been index 0 in the unrotated array. The second was adapted to work around that rotational index, and return the index of the target value.

My time complexity is O(2 * log(n)) ~ O(log(n))
My space complexity is O(10) ~ O(1), because my algorithm creates less than ten variables no matter the size of the array, so space complexity is constant.