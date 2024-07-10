# Trees
# all values to the left are less than 
# all values to the right must be greater than 
# depth is how many levels deep ...im into deep .. still havent figured out how to get access into my laptop and the desktop i have is old!!!!! #manufactored unlock mode...bruhh


class Node:

    def __init__(self, val):
        self.val = val 
        
        self.left = None
        self.right = None
        
    class BST:
        def __init__(self):
            self.root = None
            
        def insert(self, val):
            new_node = Node(val)
            if self.root is None:
                self.root = new_node
            else:
                current = self.root
                while True:
                    if val < current.val:
                        if current.left is None:
                            current.left = new_node
                            return self
                        current = current.left
                    else:
                        if current.right is None:
                            current.right = new_node
                            return self
                            current = current.right
                        
    def lookup(self, val):
        if self.root is None:
            return False
        current = self.root
        while current:
            if val < current.val:
                current = current.left
            elif val > current.val:
                current = current.right
            elif current.val == val:
                return current
        return False              
        