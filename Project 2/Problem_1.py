# Template provided by Udacity
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.num_elements = 0
        self.dict = {}
        # First dictionary key accessed
        self.first = None
        # Last dictionary key accessed
        self.latest = None

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.dict:
            prev = self.dict[key][1]
            next = self.dict[key][2]
            if next != None:
                # the last element is NOT being changed, meaning everything must be modified in some way
                if prev == None:
                    # if key being set is the first
                    self.dict[next][1] = None
                    self.first = next
                else:
                    #if key being set is not the first
                    self.dict[next][1] = prev
                    # if key being set is not the last
                    self.dict[prev][2] = next
                    
                self.dict[key][1] = self.latest
                self.dict[key][2] = None
                self.dict[self.latest][2] = key
                self.latest = key
            return self.dict[key][0]
        else:
            return -1

    def set(self, key, value):
        # Time Complexity: O(1)
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key == None:
            # This is to prevent a None key value from breaking the remove_first() function
            return
        if key in self.dict:
            prev = self.dict[key][1]
            next = self.dict[key][2]
            if next != None:
                # the last element is NOT being changed, meaning everything must be modified in some way
                if prev == None:
                    # if key being set is the first
                    self.dict[next][1] = None
                    self.first = next
                else:
                    #if key being set is not the first
                    self.dict[next][1] = prev
                    # if key being set is not the last
                    self.dict[prev][2] = next
                    
                self.dict[key][1] = self.latest
                self.dict[key][2] = None
                self.dict[self.latest][2] = key
                self.latest = key

            self.dict[key][0] = value
        
        else:
            # If the key is not already in the dictionary
            if self.first == None:
                # first key assigned to dictionary
                self.dict[key] = [value, None, None]
                self.first = key
                self.latest = key
            else:
                self.dict[key] = [value, self.latest, None]
                self.dict[self.latest][2] = key
                self.latest = key
            
            self.num_elements += 1
            if self.num_elements > self.capacity:
                self.remove_first()

    def remove_first(self):
        # This function will take ( 2 x O(1) + 2 x O(1) + O(1) ) = O(5) ~ O(1)
        next = self.dict[self.first][2]
        self.dict[next][1] = None
        self.dict.pop(self.first)
        self.first = next

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached its capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
cache_1 = LRU_Cache(5)
cache_1.set(None, "shouldn't work")
print(cache_1.get(None)) # -1

# Test Case 2
cache_2 = LRU_Cache(5)
cache_2.set(10000000000000000, 1)
print(cache_2.get(10000000000000000)) # 1
cache_2.set(1, 10000000000000000)
print(cache_2.get(1)) # 10000000000000000
cache_2.set("", "empty string")
print(cache_2.get("")) # empty string

# Test Case 3 (Takes a few seconds to run)
cache_3 = LRU_Cache(10000000)
for n in range(10000000):
    cache_3.set(n, n*5)
print("Cache_3 current number of elements: ", cache_3.num_elements)
print("Cache_3 max capacity: ", cache_3.capacity)
print("Is cache_3 at capacity? ", cache_3.num_elements == cache_3.capacity)
print(cache_3.get(0)) # 0
print(cache_3.get(1)) # 5
print(cache_3.get(2)) # 10
print(cache_3.get(3)) # 15
cache_3.set("one more", 4000)
print(cache_3.get("one more")) # 4000
# Key 5 should be deleted because of capacity overflow
print(cache_3.get(4)) # -1