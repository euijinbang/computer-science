import queue

# queue
normal_queue = queue.Queue()
normal_queue.put("coding")
normal_queue.put("first")
normal_queue.qsize()
normal_queue.get()  #coding
normal_queue.qsize()

# lifoqueue
lifo_queue = queue.LifoQueue()
lifo_queue.put("coding")
lifo_queue.put("first")
lifo_queue.qsize()
lifo_queue.get()    #first 
lifo_queue.qsize()

# priorityqueue
priority_queue = queue.PriorityQueue()
priority_queue.put((10, "coding"))  #priority, data in tuple
priority_queue.put((5, "first"))
priority_queue.put((1, "mind"))
priority_queue.qsize()
priority_queue.get()    #mind


# list 로 구현
queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

for i in range(10):
    enqueue(i)

print(len(queue_list))
enqueue(33)
print(queue_list)
dequeue()
print(queue_list)