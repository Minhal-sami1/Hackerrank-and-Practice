class Node():
    def __init__(self, value = None):
        # Defining some basic node elements
        self.value = value
        self.left_child = None
        self.right_child = None
class Binary_tree:
    def __init__(self):
        # By Default the root would be none, we will use it later
        self.root = None
    def insert(self, value):
        # if self.root is empty then the provided value would be its default
        if self.root == None:
            self.root = Node(value)
        else:
            # if root not empty then we will use a private function to check and insert the value
            self._insert(value, self.root)
    def _insert(self, value, curr):
        if value < curr.value:
            if curr.left_child == None:
                curr.left_child = Node(value)
            else:
                self._insert(value, curr.left_child)
        elif value > curr.value:
            if curr.right_child == None:
                curr.right_child = Node(value)
            else:
                self._insert(value, curr.right_child)
        else:
            print("Already Present")