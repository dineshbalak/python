
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class Dlinkedlist:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if self.head == None:
            new_node = Node(data)
            new_node.next = None
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.next = None
            new_node.prev = cur
    
    def prepend(self, data):
        if self.head == None:
            new_node = Node(data)
            new_node.next = None
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

mylist = Dlinkedlist()
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.prepend(4)
mylist.print_list()

