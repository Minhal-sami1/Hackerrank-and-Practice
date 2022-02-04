import sys


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

    def levelOrder(self, root, target):
        # Write your code here
        global level
        resulta = self._levelOrder(root, target)
        print(resulta)

    def _levelOrder(self, root, target):
        global level
        curr = root
        while True:
            if curr != None:
                data = curr.data
                if target == data:
                    return level
                elif target > data:
                    level += 1
                    curr = curr.right
                elif target < data:
                    level += 1
                    curr = curr.left
            else:
                print("Not Found!")


global level
level = 1
T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
target = int(input())
myTree.levelOrder(root, target)
