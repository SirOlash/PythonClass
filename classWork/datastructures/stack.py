class Stack:
    def __init__(self):
        self.stack = [None] * 4
        self.stack_size = 0

    def is_empty(self):
        return self.stack_size == 0

    def push(self, element):
        self.stack[self.stack_size] = element
        self.stack_size += 1

    def size(self):
        return self.stack_size

    def peek(self):
        return self.stack[self.stack_size - 1]

    def pop(self):
        if self.stack_size == 0:
            return "Stack is empty. Cannot pop."
        self.stack[self.stack_size - 1] = None
        self.stack_size -= 1

    def search(self, element):
        count = self.stack_size
        for word in self.stack:
            if word == element:
                return count
            count -= 1
        return -1



