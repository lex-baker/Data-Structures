# Problem 2

This was an easy one to solve, as each recursive instance just had to return an array of the paths to files that matched the suffix, 
and concatenate them all in the end.

Time complexity is relative to the depth of directories and number of files.

Where n is the number of directories and s is the size of each directory: time complexity = O(n * s)


Space complexity depends on how many files are found.
Where n is the number of files found: space complexity = O(n * path_string_size)