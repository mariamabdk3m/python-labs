import pickle

class QueueOutOfRangeException(Exception):
    pass

class EnhancedQueue:
    instances = {}

    def __init__(self, name, max_size):
        self.name = name
        self.max_size = max_size
        self.items = []
        EnhancedQueue.instances[name] = self

    def enqueue(self, value):
        if len(self.items) >= self.max_size:
            raise QueueOutOfRangeException(f"Queue '{self.name}' is out of range.")
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            print("Warning: Attempt to dequeue from an empty queue.")
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    @classmethod
    def get_queue(cls, name):
        return cls.instances.get(name)

    @classmethod
    def save(cls, filename):
        with open(filename, 'wb') as f:
            pickle.dump(cls.instances, f)

    @classmethod
    def load(cls, filename):
        with open(filename, 'rb') as f:
            cls.instances = pickle.load(f)

if __name__ == "__main__":

    queue1 = EnhancedQueue("TestQueue", 3)
    queue1.enqueue(1662001)
    queue1.enqueue(16122000)


    try:
        queue1.enqueue(165613)
        queue1.enqueue(3427)  
    except QueueOutOfRangeException as e:
        print(e)

    print(queue1.dequeue())  
    print(queue1.dequeue()) 
    print(queue1.dequeue())  


    EnhancedQueue.save("queues.dat")


    EnhancedQueue.load("queues.dat")
    

    loaded_queue = EnhancedQueue.get_queue("TestQueue")
    if loaded_queue:
        print(loaded_queue.items)  