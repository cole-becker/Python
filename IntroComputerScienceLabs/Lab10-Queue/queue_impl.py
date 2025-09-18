# ADD YOUR IMPLEMENTATION OF THE Queue CLASS HERE

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Queue empty.")
        
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("dequeue() called on empty queue")
        
    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return " ".join(map(str, self.queue))

queue = Queue()
print(f'{queue.is_empty() = }')             # True
print(f'empty: {queue}')                    # [ ]
queue.enqueue(10)
print(f'after enqueue(10): {queue}')        # [ 10 ]
print(f'is_empty(): {queue.is_empty()}')    # False
queue.enqueue(1)
print(f'after enqueue(1): {queue}')         # [ 10 1 ]
print(f'dequeue(): {queue.dequeue()}')      # 10
print(f'after dequeue(): {queue}')          # [ 1 ]
queue.enqueue(2)
print(f'after enqueue(2): {queue}')         # [ 1 2 ]
queue.enqueue(3)
print(f'after enqueue(3): {queue}')         # [ 1 2 3 ]
queue.enqueue(4)
print(f'after enqueue(4): {queue}')         # [ 1 2 3 4 ]
print(f'dequeue(): {queue.dequeue()}')      # 1
print(f'after dequeue(): {queue}')          # [ 2 3 4 ]
print(f'dequeue(): {queue.dequeue()}')      # 2
print(f'after dequeue(): {queue}')          # [ 3 4 ]
print(f'dequeue(): {queue.dequeue()}')      # 3
print(f'after dequeue(): {queue}')          # [ 4 ]
print(f'dequeue(): {queue.dequeue()}')      # 4
print(f'after dequeue(): {queue}')          # [ ]
print(f'is_empty(): {queue.is_empty()}')    # True