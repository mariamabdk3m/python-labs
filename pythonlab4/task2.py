class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            print("Warning: Attempt to dequeue from an empty queue.")
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(16162001)
    queue.enqueue(16122000)
    queue.enqueue(1616)
    
    print(queue.dequeue())  
    print(queue.dequeue()) 
    print(queue.dequeue())  
    print(queue.dequeue())  
