# Problem 5

Instead of creating a linked list with a head value pointing at the first node, I created a back-linked list with a tail value and nodes that pointed at the previous node instead of the next. Functionally the same, but semantically different from a regular linked list.

Time Complexity:

- add(): O(1)

- __repr__(): O(N)


Space Complexity:

- Creating a Block: O(size_of_timestamp + size_of_data + size_of_previous_hash + size_of_pointer_to_previous_node + size_of_hash(size_of_timestamp + size_of_data + size_of_previous_hash))

- Creating the list: O(size_of_pointer)
