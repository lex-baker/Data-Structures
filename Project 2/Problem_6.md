# Problem 6

I used a dictionary for both the union and intersection functions to map which values had been used already and which hadn't in an efficient way. 

For union, all non-duplciate values of the first list are added to the dictionary and the linked list, then for every value of the second list that isn't in the dictionary is added to the linked list, then the dictionary (to prevent duplications).

For intersection, all non-duplciate values of the first list are added to the dictionary, then every value of the second linked list that is in the dictionary is added to the linked list, then removed from the dictionary to prevent duplicates.

Time complexity:

- union(): where f is the size of the first list and s is the size of the second list, O(f + s) ~ O(2n)

- intersection(): where f is the size of the first list and s is the size of the second list, O(f + s) ~ O(2n)