# Problem 6

I may have misread the problem, but finding only the max and min of a function in a single traversal and O(n) time is pretty simple, provided I did it correctly and am not overlooking something major.

For creating the O(n) sorting algorithm, I made three iterations and left them all well-commented.

---

For min/max:

Time complexity: O(n), and in a single traversal

Space complexity: O(1)

---

For initial sort algorithm:

Time complexity: O(2 * n) ~ O(n)

Space complexity: O(n)

---

For intermediate sort algorithm:

Time complexity: O(4 * n) ~ O(n); Total n's come from: min/max, create array of None, fill array, create final array that leaves out None's.

Space complexity: O(n + (range between values of array)) ~ O(n); Maybe more, not sure how to calculate the possibly much larger range between values

---

For final sort algorithm:

Time complexity: O(4 * n); Same as intermediate, because even though duplicated values are being interacted with, the total number of values doesn't exceed the original array's length
Space complexity: O(n + (range between values of array)) ~ O(n); Same as intermediate, still not sure how to calculate.