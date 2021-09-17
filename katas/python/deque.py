"""
collections.deque uses an implementation of a linked list in which you can access, insert, or 
remove elements from the beginning or end of a list with constant O(1) performance
"""

from collections import deque

llist = deque("abcdef")
llist.append("ghi")
llist.appendleft("Start")

print(llist)