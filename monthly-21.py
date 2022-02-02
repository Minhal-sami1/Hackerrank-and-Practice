class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        if root != None:
            return self._height(root, 0)-1
        else:
            return 0
    def _height(self, curr_node, curr_height):
        if curr_node == None: return curr_height
        left_height = self._height(curr_node.left, curr_height+1)  
        right_height = self._height(curr_node.right, curr_height+1)
        return max(left_height, right_height)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       