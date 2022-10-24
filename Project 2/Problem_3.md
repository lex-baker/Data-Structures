# Problem 3

This was a tricky problem to solve, and took me roughly five hours to land a solution that worked. I debated about what data structure to use, eventually deciding on an ordered Linked List with Frequency Nodes, or nodes that stored a letter and frequency. This made it easy to fill in the list with the Huffman Nodes, which stored a number and its two children nodes.

Time complexity isn't great in the worst-case. Here it is for each function:

- add(): where i is the index of the letter being added, O(i)

- pop(): O(1)

- convert_to_huffman(): where d is number of nodes in the linked list, O(d). However, n is rapidly shrinking, and typically wouldn't be larger than 26 (lowercase letters) + 26 (captial letters) = 52

- create_translation() --> search(): O(1), as every action in the recursive function works in constant time 

- encode(): where n is length of string to encode, O(n)

- decode(): where n is length of string to decode, O(n)

- huffman_encoding(): where n is number of characters in string to encode, O( n * O(i) + O(d) + O(n) ) ~ O( 2n * O(i) ) ~ O( n * O(i) )

- huffman_decoding(): where n is length of string to decode, O( O(n) ) = O(n)