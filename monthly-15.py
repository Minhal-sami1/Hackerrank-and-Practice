class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self, head, data):
        # check if head is none
        if head == None:
            # store the data in the Node class in a variable called head
            head = Node(data)
            # self.tail will store the value of head beacause eventually head will be none again
            self.tail = head
        # if head is not None
        else:
            # Store the data in the Node class in a variable called new_node
            new_node = Node(data)
            # self.tail refers to the "head" which means it is the previous node than this one
            self.tail.next = new_node
            # now the self.tail will be equal to the current node
            self.tail = new_node
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  