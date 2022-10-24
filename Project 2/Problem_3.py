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
            
            # print(self)
        
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
    if data == None or data == "":
        print("Can't encode an empty string!")
        return None, PriorityLinkedList()
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
    if data == None or data == "":
        print("Can't decode an empty string!")
        return None 
    return tree.decode(data)

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
# First result when googling "long story"
encoded, tree = huffman_encoding("""I HAVE SOME GOOD news. Next month, The Atlantic will once again send fiction home to our subscribers, in a special supplement that will accompany our May issue. On the newsstand, the supplement will be bound into the May magazine.

The short story has been integral to The Atlantic since our first issue, in 1857, in which we published four stories, including “The Mourning Veil,” by Harriet Beecher Stowe. But as longtime, generously loyal readers know, for the past five years we have published fiction once a year in a special newsstand issue, rather than in any of our 10 subscriber issues. During what has been widely noted to be a “challenging” (read: harrowing) business environment for publishing, this has been a necessary compromise. But none of us has been particularly happy with it, and we have been searching for ways to once again place great fiction in front of all our readers.

With our fiction issue last year, we began a partnership with Luminato, the Toronto Festival of Arts and Creativity, which shares our love of literature. Building on the success of that first outing, which included participation by some of our editors and authors in the festival, we have jointly decided this year to raise our ambition by creating the supplement, which will include, along with half a dozen short stories, a powerful essay on writing and loss by Joyce Carol Oates. We think—we hope!—we are seeing renewed interest in the short story. Last fall, we started a digital fiction series, publishing to the Amazon Kindle two short stories a month by authors like Christopher Buckley, Curtis Sittenfeld, and Paul Theroux. All told, The Atlantic is now publishing more fiction than it has since the mid-1970s.

But I should admit that these fiction initiatives are experimental, provisional, part of our larger adventure through the seismically shifting landscape of letters. If our hardworking developers have pulled it off, by the time you read this note our Web site, TheAtlantic.com, will have relaunched with a new design and a superior system for finding the subjects you’re interested in and discovering new ideas you didn’t know you were looking for. We’ve also released two apps for the iPhone so far and are about to release a third, much improved, one.

We are experimenting busily, in other words, with any new technology that emerges in this extraordinarily fertile era. If it looks like we’re making things up as we go along, the reason is that we are. To each “platform,” as they are now called in the trade, we are tailoring the Atlantic work that can fit it best—trying to help you make sense of the world, to keep you informed and entertained, through whatever medium you find most congenial. For our print magazine and our e-reader editions, we are continuing to devote months of reporting and writing to create pieces like Joshua Green’s profile in this issue of Treasury Secretary Timothy Geithner, and Robert D. Kaplan’s assessment of the war in Afghanistan. For the Web site each day, we produce dozens of posts analyzing breaking developments in politics, business, culture, technology, and other subjects, some of them longtime preoccupations of The Atlantic, others fairly new to all of us. As I write, on our site I can see posts popping up by James Fallows about Twitter, by Andrew Sullivan about the future of gays in the military, and by Ta-Nehisi Coates about the moral courage of Civil War General George Henry Thomas.

What matters to us—in all the work that we do, on whatever platform may present itself—is the quality and consequence of an idea, and the clarity and power of its expression. We believe, and we believe that you believe, that of the many and proliferating means for communicating big ideas, one of the most effective, and therefore most enduring, is fiction.""")
print(encoded)
decoded = huffman_decoding(encoded, tree)
print(decoded) # Should return the input, I don't want to paste all of that again.

# Test Case 2
encoded, tree = huffman_encoding("")
print(encoded) # None
decoded = huffman_decoding(encoded, tree)
print(decoded) # None

# Test Case 3
encoded, tree = huffman_encoding("Udacity Mission Statement - Udacity is the trusted market leader in talent transformation. We change lives, businesses, and nations through digital upskilling, developing the edge you need to conquer what's next.")
print(encoded)
decoded = huffman_decoding(encoded, tree)
print(decoded)