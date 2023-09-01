#queue in python

queue = []

#adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')

print('Initial queue: ')
print(queue)

#Removing all elements from queue
print('\nElements dequeued from queue')
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

#uncommenting print(queue.pop(0))
#will raise an index error
#as queue is empty now

