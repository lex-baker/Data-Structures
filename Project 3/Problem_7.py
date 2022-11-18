# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler, null_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        # Set our root node's handler to the root_handler response
        self.root.handler = root_handler
        # Define a "null response" handler for when a node is not found or doesn't have a defined handle is not found
        self.null_handler = null_handler

    def insert(self, paths, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        
        # Start with root node
        node = self.root
        # For each path word in paths
        for path in paths:
            # Insert logic as handled by the RouteTrieNode class
            node.insert(path)
            node = node.children[path]
            # Set every node after the root's handler to the null_handler value
            node.handler = self.null_handler
        # Set the final node's handler to the parameter given
        node.handler = handler


    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        for path in paths:
            if path in node.children:
                node = node.children[path]
            else:
                return self.null_handler
        return node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, path):
        # Insert the node as before
        if path not in self.children:
            self.children[path] = RouteTrieNode()




# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, null_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!

        # Init the RouteTrie
        self.trie = RouteTrie(root_handler, null_handler)


    def add_handler(self, route, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

        # Paths is an array of words that make up the path
        paths = self.split_path(route)
        # Hand off the paths and handler to RouteTrie for heavy lifting
        self.trie.insert(paths, handler)

    def lookup(self, route):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        # Paths is an array of words that make up the path
        paths = self.split_path(route)
        # Pass off the paths to the RouteTrie
        found_handler = self.trie.find(paths)
        # Return result, which will be a handler
        return found_handler



    def split_path(self, route):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        # Add route path

        # Strip leading and trailing "/" from route
        route = route.strip("/")
        
        if route == "":
            # If route is now empty, make paths empty (for simplicity)
            paths = []
        else:
            # Otherwise split by "/"
            paths = route.split("/")

        return paths


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

# My tests
print("\nMy test and edge cases:\n")

router.add_handler("/home/about/me/", "about me handler")
print(router.lookup("/home/about/me")) # should print 'about me handler'

print(router.lookup("")) # should print 'root handler'
# This is because "/" and "" should be the same, because www.example.com/ and www.example.com should bring the user to the same place

router.add_handler("/", "new root handler") # Updating the root handler
print(router.lookup("/")) # should print 'new root handler'

print(router.lookup("")) # should also print 'new root handler'

print(router.lookup("/does/not/exist")) # should print 'not found handler'