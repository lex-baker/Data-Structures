class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head == None:
            return ""
        cur_head = self.head
        out_string = ""
        while cur_head.next:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        out_string += str(cur_head.value)
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    values = set()
    united = LinkedList()
    node = llist_1.head
    while node != None:
        if node.value not in values:
            values.add(node.value)
            united.append(node.value)
        node = node.next

    node = llist_2.head
    while node != None:
        if node.value not in values:
            united.append(node.value)
            values.add(node.value)

        node = node.next
    return united

def intersection(llist_1, llist_2):
    # Your Solution Here
    values = set()
    intersected = LinkedList()
    node = llist_1.head
    while node != None:
        if node.value not in values:
            values.add(node.value)
        node = node.next

    node = llist_2.head
    while node != None:
        if node.value in values:
            intersected.append(node.value)
            values.remove(node.value)
        node = node.next
    return intersected


# Example 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print ("Union:", union(linked_list_1,linked_list_2)) # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 -> 1
print()
print ("Intersection: ", intersection(linked_list_1,linked_list_2)) # 6 -> 4 -> 21
print()

# Example 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ("Union:", union(linked_list_3,linked_list_4)) # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1
print()
print ("Intersection: ", intersection(linked_list_3,linked_list_4)) # <<Nothing>>
print()

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print ("Union:", union(linked_list_1,linked_list_2)) # <<Nothing>>
print()
print ("Intersection: ", intersection(linked_list_1,linked_list_2)) # <<Nothing>>

print("\n")

# Test Case 2
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = []

for i in range(50):
    linked_list_1.append(i)

for i in range(25, 75):
    linked_list_2.append(i)

print ("Union:", union(linked_list_1,linked_list_2)) # 25 -> .. -> 49 where .. is every element in between
print()
print ("Intersection: ", intersection(linked_list_1,linked_list_2)) # 0 -> .. -> 74 where .. is every element in between
print("\n")

# Test Case 3
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [None, 0, None]
element_2 = [None, 0, 1, 1, None]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print ("Union:", union(linked_list_1,linked_list_2)) # None -> 0 -> 1
print()
print ("Intersection: ", intersection(linked_list_1,linked_list_2)) # None -> 0