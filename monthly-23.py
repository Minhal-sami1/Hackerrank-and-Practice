from os import lstat
import queue
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

    def levelOrder(self, root):
        # Write your code here
        # Take all elements
        if root != None:
            test = self._levelOrder(root)
        pass

    def _levelOrder(self, root):
        cnt = 0
        que = []
        if root != None:
            que.append(root)
        while(True):
            if not que:
                break
            curr = que.pop(0)
            print(curr.data, end=" ")
            if curr.left != None:
                que.append(curr.left)
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
