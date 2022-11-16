# Problem 2

I used two binary searches, the first of which found the "rotational index" or which index of the rotated array would've been index 0 in the unrotated array. The second was adapted to work around that rotational index, and return the index of the target value. Originally, I tried to make the second binary search work around the pivot, and almost got it working, but got stuck trying to reason what the end of the while loop should look like, in the event the number/target isn't found. After spending a few hours working on other problems, I realied I could do a single step of the binary search manually, then pass off the "side" of the pivot that the number was in to make my life easier.

My time complexity is O(2 * log(n)) ~ O(log(n))
My space complexity is O(10) ~ O(1), because my algorithm creates less than ten variables no matter the size of the array, so space complexity is constant.