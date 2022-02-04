class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while(start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        # * Concept Explained here: https://www.youtube.com/watch?v=dhLtP3UriEU
        # Making so I can iterate over each value
        current = head
        # do it until they are empty
        while current and current.next:
            # if current node's data is same as next one then skip the next one and move on to another one, * EX: 1,2,2,4 : jump or skip single two and go to the next one: 1,2,4
            if current.data == current.next.data:
                current.next = current.next.next
            # Go to the next node
            else:
                current = current.next
        # Return the linked list
        return head


global T
mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head)
