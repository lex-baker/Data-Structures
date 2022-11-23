# Problem 5

All work was done both on the online Jupyter Notebook as well as the included Trie.ipynb file. 

I used a Trie class in conjunction with the individual TrieNode class. I created a second recursive function "helper" because I was struggling to get the all_suffixes variable to not become [[[['suffix']]]], and while a more elegant solution may exist, my code works in an understandable way with minimal workarounds.


TrieNode:

- Init:
    - Time Complexity: O(1)
    - Space Complexity: O(1)

- Insert:
    - Time Compexity: O(n)
    - Space Complexity: O(1)

- Suffixes and Recurse_Suffix:
    - Time Compexity: O(n^n); because you have to iterate through all children of every node, and all children of every child.
    - Space Complexity: O(n^n); because in the worst-case every node is both a word end and has children.

Trie:

- Init:
    - Time Compexity: O(1)
    - Space Complexity: O(1)

- Insert:
    - Time Compexity: O(n^2)
    - Space Complexity: O(n)

- Find:
    - Time Compexity: O(n^n); because every child must be iterated through to find correct one, then every child of that node, and so on.
    - Space Complexity: O(n); because variables are only being created or modified when the correct node is found, not for every node iterated.