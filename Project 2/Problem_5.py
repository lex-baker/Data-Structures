import hashlib
import time

class Block:

    def __init__(self, data, previous_node, previous_hash):
      self.timestamp = time.time()
      self.data = data
      self.previous_hash = previous_hash
      self.previous = previous_node
      self.hash = self.calc_hash(data + str(self.timestamp) + (previous_hash or 'None'))
    
    def calc_hash(self, hash_str):
        sha = hashlib.sha256()

        #hash_str = "We are going to encode this string of data!".encode('utf-8')
        #print(hash_str.encode('utf-8'))
        sha.update(hash_str.encode('utf-8'))

        return sha.hexdigest()
    
    def __repr__(self):
        return f"Node(\n\t{self.data}\n\tcurrent hash: {self.hash}\n\tand previous hash: {self.previous_hash}\n)\n"


class Blockchain:
    def __init__(self):
        self.tail = None
    
    def add(self, data):
        if self.tail == None:
            self.tail = Block(data, None, None)
            return
        
        self.tail = Block(data, self.tail, self.tail.hash)

    def __repr__(self):
        output = ""
        node = self.tail
        while node != None:
            output = str(node) + output
            node = node.previous
        return output
        

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
blockchain = Blockchain()
blockchain.add("Hello there")
blockchain.add("More data")
blockchain.add("Same data")
blockchain.add("Same data")
blockchain.add("Final data")
print(blockchain)
node = blockchain.tail
while node != None:
    print(node.data, "|", end=" ") # Final data | Same data | Same data | More data | Hello there |
    node = node.previous
print()

# Test Case 2
# Each should have a different hash
blockchain = Blockchain()
blockchain.add("")
blockchain.add("")
blockchain.add("")
print(blockchain)
node = blockchain.tail
while node != None:
    print(node.data, "|", end=" ") #  |  |  |  # Because all are empty
    node = node.previous
print("\n")
# Test Case 3
blockchain = Blockchain()
for i in range(1000):
    blockchain.add(str(i))
node = blockchain.tail
while node != None:
    print(node.data, "|", end=" ") # Counting down by four, from 999 to 0. Expected output: 999 | 994 | ... | 9 | 4 |
    node = node.previous.previous.previous.previous.previous