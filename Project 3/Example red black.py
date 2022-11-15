# Node and Tree structures, with help from the earlier lesson on Red-Black Trees.
class Node():
    def __init__(self, value, parent, is_red):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        #self.color = color
        self.red = is_red

    # Returns node's grandparent
    def grandparent(self):
        if self.parent == None:
            return None
        return self.parent.parent

    # Returns node's parent's sibling
    def pibling(self):
        gp = self.grandparent(self.parent)
        if gp == None:
            return None
        if self.parent == gp.right:
            return gp.left
        if self.parent == gp.left:
            return gp.right


class RedBlackTree():
    def __init__(self, root):
        self.root = Node(root, None, True)
        
    def insert(self, new_val):
        new_node = self.insert_helper(self.root, new_val)
        self.balance(new_node)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                return self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val, current, True)
                return current.right
        else:
            if current.left:
                return self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val, current, True)
                return current.left

    def balance(self, node):    
        if not node.parent or not node.parent.red:
            return
        
        if node.pibling() and node.pibling().red == True:
            node.grandparent().red = True
            node.pibling().red = False
            node.parent.red = False
            return self.balance(node.grandparent())
        
        gp = node.grandparent()        
        if gp == None:
            return
        
        if gp.left and node == gp.left.right:
            self.rotate_left(node.parent)
            node = node.left
        elif gp.right and node == gp.right.left:
            self.rotate_right(node.parent)
            node = node.right

        p = node.parent
        gp = p.parent
        if node == p.left:
            self.rotate_right(gp)
        else:
            self.rotate_left(gp)
        p.red = False
        gp.red = True

    def rotate_left(self, node):
        # Grab the parent
        p = node.parent

        # the given node's right child is moving up
        changing = node.right
        # The node's right child is the node's right child's left child
        node.right = changing.left

        # node becomes its right child's left node, and the node's parent is set to the changing node
        changing.left = node
        node.parent = changing

        # Connecting to the sub-tree's parent
        if p != None:
            if node == p.left:
                p.left = changing
            else:
                p.right = changing
        changing.parent = p

    def rotate_right(self, node):
        # Grab the parent
        p = node.parent

        # move the left child's right node to the left node's place
        changing = node.left
        node.left = changing.right

        # make the node it's left child's right child, and make the node's parent its former left child
        changing.right = node
        node.parent = changing

        # Connecting to the sub-tree's parent
        if p != None:
            if node == p.left:
                p.left = changing
            else:
                p.right = changing
        changing.parent = p

