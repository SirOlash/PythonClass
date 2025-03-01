class Set:
    def __init__(self):
        self.set = [None] * 5
        self.set_size = 0

    def is_empty(self):
        return self.set_size == 0

    def add(self, element):
        if element in self.set:
            return
        if self.size() == len(self.set):
            new_elements = [None] * (len(self.set) * 2)
            new_elements[:self.set_size] = self.set
            self.set = new_elements
        self.set[self.set_size] = element
        self.set_size += 1

    def size(self):
        return self.set_size

    def remove(self, element):
        for i in range(self.set_size):
            if self.set[i] == element:
                for j in range(i, self.set_size - 1):
                    self.set[j] = self.set[j + 1]
                self.set[self.set_size - 1] = None
                self.set_size -= 1


    def get_element_by_index(self, index):
        return self.set[index]

    def get_index_by_element(self, element):
        for i in range(self.set_size):
            if self.set[i] == element:
                return i
        return -1

    def contains(self, element):
        return element in self.set

    def clear(self):
        self.set_size = 0
