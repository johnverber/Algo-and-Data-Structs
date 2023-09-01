#queue implementation
#using colllections.deque

from collections import deque

#initializing a queue
q = deque()

#adding elements to a queue
q.append('a')
q.append('b')
q.append('c')

print('Initial queue')
print(q)

#removing elements from queue
print('\nElements dequeued from the queue')
print(q.popleft())
print(q.popleft())
print(q.popleft())

print('\nQueue after removing elements')
print(q)

#uncommenting q.popleft()
#will raise IndexError
#as queue is now empty

"""There are various functions available in this module: 
 

maxsize – Number of items allowed in the queue.
empty() – Return True if the queue is empty, False otherwise.
full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
qsize() – Return the number of items in the queue."""