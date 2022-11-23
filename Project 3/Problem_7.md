# Problem 7

I used a slightly modified Trie class as well as the TrieNode class, which were wrapped into the Router class. Most of this problem was a repeat from Problem 5, but a bit more challenging since now I was working through a wrapper. I enjoyed this problem quite a bit, because it reminded me of the week straight that I had spent configuring a local Nginx server. That definitely helped me understand what was going on here, as a path is just the names of folders you walk through on your way to the file to be served.


RouteTrieNode:

- Init:
    - Time Complexity: O(1)
    - Space Complexity: O(1)

- Insert:
    - Time Compexity: O(n)
    - Space Complexity: O(1)


RouteTrie:

- Init:
    - Time Compexity: O(1)
    - Space Complexity: O(1)

- Insert:
    - Time Compexity: O(n^2); because the method itself seems to run in O(n), but calls a method that also takes O(n) time, n times.
    - Space Complexity: O(n)

- Find:
    - Time Compexity: O(n^2)
    - Space Complexity: O(n); because variables are only being created or modified when the correct node is found, not for every node iterated.


Router:

- Init:
    - Time Compexity: O(1)
    - Space Complexity: O(1)

- Add_Handler:
    - Time Compexity: O(n^2)
    - Space Complexity: O(n)

- Lookup:
    - Time Compexity: O(n^2)
    - Space Complexity: O(n)

- Split_Path:
    - Time Compexity: O(1)
    - Space Complexity: O(1)