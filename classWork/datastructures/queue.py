class Queue:
    def __init__(self):
        self.queue = [None] * 3
        self.queue_size = 0

    def is_empty(self):
        return self.queue_size == 0

    def add(self, element):
        self.queue[self.queue_size] = element
        self.queue_size += 1

    def size(self):
        return self.queue_size

    def offer(self, element):
        if self.queue_size == len(self.queue):
            return False
        self.queue[self.queue_size] = element
        self.queue_size += 1
        return True

    def poll(self):
        if self.queue[0] is not None:
            for i in range(1, self.queue_size):
                self.queue[i - 1] = self.queue[i]
            self.queue[self.queue_size - 1] = None
            self.queue_size -= 1
            return self.queue[0]
        return None

    def peek(self):
        return self.queue[0]
