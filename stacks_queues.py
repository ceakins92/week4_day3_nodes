# list - time complexity
# searching is linear O(N)
# [12,3,59,4,19].index(4)
# indexing into a list is constant O(1)
# [3,6,18,10][3]
# copy a list O(N)
# [1,3,9][:]
# adding to a list is constant O(1)
# [1,2,3].append(4)
# removing from the end is constant O(1)
# [1,2,3].pop()
# removing from specific position is linear O(N)
# [1,2,3,4,5,6,7].pop(2)

# stack - last in, first out.  Like a can of pringles
stack = []
stack.append(1)  # O(1)
stack.append(2)  # O(1)
stack.append(3)  # O(1)
# implement stack .pop()
stack.pop() # O(1)


# queue - first in, first out.  Like a person getting in line
queues = []
queues.append(1)  # O(1)
queues.append(2)  # O(1)
queues.append(3)  # O(1)
# remove first (0 is last in a queue)
queues.pop() # O(N)
# using insert becomes linear
queues.insert(0,1) # O(N)
# remove first
queues.pop(1) # O(N)