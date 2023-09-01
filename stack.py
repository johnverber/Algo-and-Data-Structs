#stack

stack = []

#append() function to puch
#element to stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial Stack')
print(stack)


#pop() function top pop 
#element from stock
#lifo order
print("\nElements popped from stack: ")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("\nStack after all elements are popped: ")
print(stack)

#uncommenting print(stack.pop())
#will cause an IndexError
#as the stack is now empty

