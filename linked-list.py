# * This is a single node, Node is an item of linked list. It contains the data plus refernce to the next item in linked list
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
# this is an starting of the Linkedlist or Paticularly called Head
class Linkedlist:
    def __init__(self):
        self.head = None
if __name__ == '__main__':
    linked_list = Linkedlist()

    # Assigning data
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Referencing them or connecting them
    linked_list.head.next = second
    second.next = third

    # Printing the linked list
    while linked_list.head != None:
        print(linked_list.head.item)
        linked_list.head = linked_list.head.next