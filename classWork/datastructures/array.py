class Array:
    def __init__(self, initial_capacity = 5):
        self._size = 0
        self.elements = [None] * initial_capacity
        self.capacity = initial_capacity

    def is_empty(self):
        return self._size == 0

    def add(self,element):
        self.elements[self._size] = element
        self._size += 1

    def size(self):
        return self._size

    def remove(self,element):
        for i in range(self._size):
            if self.elements[i] == element:
                for index in range (i,self._size-1):
                    self.elements[index] = self.elements[index + 1]
                self.elements[self._size - 1] = None
                self._size -= 1
                break

    def contains(self,element):
        for word in self.elements:
            if word == element:
                return True
        return False





