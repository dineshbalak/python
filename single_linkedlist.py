
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Slinkedlist:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if self.head == None:
            new_node = Node(data)
            new_node.next = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.next = None
    
    def prepend(self, data):
        if self.head == None:
            new_node = Node(data)
            new_node.next = None
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def length(self):
        total = 0
        cur = self.head
        while cur:
            cur = cur.next
            total+=1
        return total

    def delete(self, index):
        if index>=self.length():
            print ("ERROR: Index out of range!")
            return
        cur_index = 0
        cur = self.head
        while True:
            last_node = cur
            cur = cur.next
            if cur_index == index:
                last_node.next = cur.next
                return
            cur_index+=1

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

mylist = Slinkedlist()
mylist.append(1)
mylist.append(4)
mylist.append(-1)
mylist.append(3)
mylist.prepend(2)
mylist.print_list()
mylist.delete(3)
mylist.print_list()
print(mylist.length())
