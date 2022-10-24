# Problem 1

I solved this by created what is essentially a doubly-linked list using a dictionary. Each key in the dictionary has an array, with the assigned value, previous entry, and next entry. 

Time complexity for this solution remains O(1), because every computation is either an array access, or a dictionary add, remove, or asscess function, all of which are O(1). Each function has its time complexity denoted with a comment


Space complexity for this solution is O(4 * integer_size + n * key_size + n * (value_size + 2 * key_size))
