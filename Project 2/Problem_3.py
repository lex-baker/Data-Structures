import sys

class FrequencyNode:
    def __init__(self, letter):
        self.next = None
        self.letter = letter
        self.frequency = 1
    def increment(self):
        self.frequency += 1
    def __int__(self):
        return self.frequency

class HuffmanNode:
    def __init__(self, node1, node2):
        self.next = None
        self.value = int(node1) + int(node2)
        if int(node1) <= int(node2):
            self.left = node1
            self.right = node2
        else:
            self.left = node2
            self.right = node1

    def __int__(self):
        return self.value


class PriorityLinkedList:
    # The closer a node is to the head, the lower its frequency
    def __init__(self):
        self.head = None
        self.encode_dict = {}
    
    def add(self, letter):
        if self.head == None:
            self.head = FrequencyNode(letter)
            return

        # If any nodes already exist
        node = self.head
        previous = None
        while node != None:
            if node.letter == letter:
                node.increment()
                if node.next == None:
                    #It's already the last value, so move on
                    return
                old_next = node.next
                new_next = node.next
                while new_next.next != None and node.frequency > new_next.next.frequency:
                    new_next = new_next.next
                #previous.next --> old_next
                if previous != None:
                    previous.next = old_next
                else:
                    # Previous node was none, meaning current node is pointed to by self.head
                    self.head = old_next
                #node.next --> new_next.next, even if nex_next.next = None
                node.next = new_next.next
                #new_next --> node
                new_next.next = node
                return

            else:
                previous = node
                node = node.next
            
        # If the letter doesn't exist in the list
        old_head = self.head
        self.head = FrequencyNode(letter)
        self.head.next = old_head
    
    def pop(self):
        node = self.head
        self.head = node.next
        return node

    def convert_to_huffman(self):
        #Turning the linked list into a binary tree
        while self.head.next != None:
            huffnode = HuffmanNode(self.pop(), self.pop())
            if self.head == None:
                self.head = huffnode
                return
            if int(huffnode) > int(self.head):
                old_next = self.head
                new_next = self.head
                while new_next.next != None and int(huffnode) > int(new_next.next):
                    new_next = new_next.next
                #previous.next --> old_next
                self.head = old_next
                #node.next --> new_next.next, even if nex_next.next = None
                huffnode.next = new_next.next
                #new_next --> node
                new_next.next = huffnode
            else:
                huffnode.next = self.head
                self.head = huffnode
            
            print(self)
        
    def create_translation(self):
        self.search(self.head, "")
    
    def search(self, root, path):
        if type(root.left) == HuffmanNode:
            self.search(root.left, path + "0")
        else:
            self.encode_dict[root.left.letter] = path + "0"
        
        if type(root.right) == HuffmanNode:
            self.search(root.right, path + "1")
        else:
            self.encode_dict[root.right.letter] = path + "1"

    def encode(self, string):
        encoded = ""
        for l in string:
            encoded += self.encode_dict[l]
        return encoded
    
    def decode(self, code):
        decoded = ""
        node = self.head
        for s in code:
            if s == "0":
                node = node.left
            else:
                node = node.right
            
            if type(node) == FrequencyNode:
                decoded += node.letter
                node = self.head
        return decoded

    def repr_search(self, root, level):
        if type(root.left) == HuffmanNode:
            print("Left - HuffmanNode(" + str(root.left.value) + ")", str(level))
            self.repr_search(root.left, level + 1)
        else:
            print("Left - FrequencyNode(" + str(root.left.letter) + ")", str(level))
        
        if type(root.right) == HuffmanNode:
            print("Right - HuffmanNode(" + str(root.right.value) + ")", str(level))
            self.repr_search(root.right, level + 1)
        else:
            print("Right - FrequencyNode(" + str(root.right.letter) + ")", str(level))

    def __repr__(self):
        node = self.head
        output = ""
        if type(node) == HuffmanNode:
            self.repr_search(self.head, 1)
        else:
            while node.next != None:
                if type(node) == FrequencyNode:
                    output += "FrequencyNode(" + str(node.letter) + ", " + str(node.frequency) + "), "
                else:
                    output += "HuffmanNode(" + str(node.value) + "), "
                node = node.next
            if type(node) == FrequencyNode:
                output += "FrequencyNode(" + str(node.letter) + ", " + str(node.frequency) + ")"
            else:
                output += "HuffmanNode(" + str(node.value) + ")"
        return output

# Returns both the encoded string and the tree used to encode it
def huffman_encoding(data):
    priority = PriorityLinkedList()
    for l in data:
        priority.add(l)
    #print(priority)

    # Turning the priority queue into a Huffman Tree
    priority.convert_to_huffman()
    #print(priority)

    # After the Huffman Tree is created, the encoding can be done automatically using a dictionary
    priority.create_translation()

    return priority.encode(data), priority

def huffman_decoding(data,tree):
    return tree.decode(data)

codes = {}

a_great_sentence = "The bird is the word"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence) 

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)))) # 36
print ("The content of the encoded data is: {}\n".format(encoded_data)) # 1110100001110111000010101101100011111110111100000111011001110000101101

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data))) # 69
print ("The content of the encoded data is: {}\n".format(decoded_data)) # The bird is the word

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

# Test Case 2

# Test Case 3