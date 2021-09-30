"""
collections.deque uses an implementation of a linked list in which you can access, insert, or 
remove elements from the beginning or end of a list with constant O(1) performance
"""

from collections import deque 

#initilizing a deque
de = deque([1, 2, 3])

# using append to insert element 
#insert 4 at the end of deque
de.append(4)

print("The deque will be after append(): ", de)

# using pop() to delete element 
de.pop()

print("The deuque will be after pop(): ", de)

de.appendleft("Complexity is O(1)")
print(de)

de.appendleft("Doubley ended Queue")
print(de)

de.popleft()
print(de)