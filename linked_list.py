#linked list implementation

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        count = 1
        current = self.head
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        while current:
            if count+1 == position:
                new_element.next = current.next
                current.next = new_element
                return
            else:
                count+=1
                current = current.next

        pass

    def delete(self, value):
        """Delete the first node with a given value"""
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current:
                if current.value == value:
                    break
                prev = current
                current = current.next
            if current == None:
                return
            prev.next = current.next
            current = None

#Test cases
#Set up some elements
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

#start setting up a linked list
l1 = LinkedList(e1)

l1.append(e2)
l1.append(e3)

#test get position
#should print 3
print("print 3",l1.head.next.value)

#test insert
l1.insert(e4,3)

#test delete
l1.delete(1)
print(l1.print())