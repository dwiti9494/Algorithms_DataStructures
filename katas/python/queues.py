from queue import Queue

# initilizing a queue
q = Queue(maxsize = 3)

# qsize() give the maxsize of Queue
print(q.qsize())

# adding of element to queue
q.put("m")
q.put("a")
q.put("d")

# return boolean for full queue
print("\n Full: ", q.full())

# removing element from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())

# return boolean for empty queue
print("\nEmpty: ", q.empty())

q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())
