queue = []

# append function to push element in queue
queue.append('g')
queue.append('h')
queue.append('i')

print('Initial queue')
print(queue)

# pop function to pop element from queue in LIFO order
print('\n Elements popped from queue: ')
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print('\n Elements popped from queue: ')
print(queue)