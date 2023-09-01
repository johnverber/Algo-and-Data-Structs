#queue operations using a doubly linked list

class Node:
    #function to initialise the node object
    def __init__(self, data):
        self.data = data #assign data
        self.next = None # initialize next as null
        self.prev = None # initialize prev as null

#queue class contains a node object
class Queue:
    #function to initialize head
    def __init__(self):
        self.head = None
        self.last = None

    #function to add an element data in the queue
    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last.next.prev = self.last
            self.last = self.last.next

    #function to remove first element and return the element from queue
    def dequeue(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp
        
    #function to return top element in queue
    def first(self):
        return self.head.data
    
    #function to return the size of the queue
    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count
    
    #function to check if the queue is empty or not
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
        
    #function to print the stack
    def printqueue(self):
        print("queue elements are: ")
        temp = self.head
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
    

if __name__ == '__main__':

    #start with empty queue
    queue = Queue()
    print("Queue operations using doubly linked list")
    #insert 4 at the end. so queue becomes 4->None
    queue.enqueue(4)
    #insert 5 at the end. so queue becomes 4->5None
    queue.enqueue(5)
    #insert 6 at end. so queue becomes 4->5->6->None
    queue.enqueue(6)
    #and finally 7 at the end
    queue.enqueue(7)
    #print the queue
    queue.printqueue()
    #print the first element
    print('\nfirst element is: ', queue.first())
    #print the queue size
    print("Size of the queue is: ", queue.size())
    #remove the first element
    queue.dequeue()
    #remove the first element
    queue.dequeue()
    #print the queue
    print('After applying dequeue() two times')
    queue.printqueue()
    #print true if queue is employe else false
    print('\nqueue is empty: ', queue.isEmpty())