class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root
    # * Concept explained in this video : https://www.youtube.com/watch?v=aM-oswPn19o

    def levelOrder(self, root):
        # Write your code here
        # Take all elements
        if root != None:
            self._levelOrder(root)

    def _levelOrder(self, root):
        # Make a que in which you will store on-working nodes of binary tree
        que = []
        if root != None:
            # At start que will only have the base element or root in it
            que.append(root)
        while(True):
            # If que is empty break
            if not que:
                break
            # The left most or the node to be worked on will be removed from que and transferred to curr
            curr = que.pop(0)
            # Print the Current Node's Data
            print(curr.data, end=" ")
            # If the current node has left child then append it first in the que
            if curr.left != None:
                que.append(curr.left)
            # If the current node has right child then append the right child in the que
            if curr.right != None:
                que.append(curr.right)


global level
level = 1
global lst
lst = []

T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
