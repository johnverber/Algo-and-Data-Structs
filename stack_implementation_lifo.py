#stack implementation using lifo queue model



from queue import LifoQueue

#initializing a stack
stack = LifoQueue(maxsize=3)

#qsize() show the number of elements
#in the stack
print(stack.qsize())

#put() function to push element in the stack
stack.put('a')
stack.put('b')
stack.put('c')

print("Full: ", stack.full())
print("Size: ", stack.qsize())

#get() function to pop 
#element from stack in 
#lifo order
print('\n Elements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())

print("\nEmpty: ", stack.empty())



#various functions now available in this module
#maxsize - number of items allowed in the queue
#empty() - Return true if the queue is empty. False otherwise.
#full() - Return true if there are maxsize items in the queue.  If the queue
#was initialized with maxsize=0(the default), then full() never returns
#true.
#get() - remove and return an item from the queue.  if the queue is empty,
#wait until an item is available.
#get_nowait() - Return an item if one is immediateluy available, else raise QueueEmpty
#put(item) - Put an item into the queue. if the queue is full, wait until a free slot
#is available before adding the item
#put_nowwait(item) - put an item into the queue without blocking.  if no free slot is immediately avaiable
# raise QueueFull
#qsize() - Return the number of items in the queue
