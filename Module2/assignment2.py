from re import S
from tracemalloc import start
import numpy as np

class ArrayList:
    def __init__(self, startcapasity = 20):
        self.array = np.zeros(startcapasity, dtype=object)
        self.length = 0
        self.buffer_left = int(startcapasity/2)
        self.size = startcapasity

    def __len__(self):
        return self.length
    
    #
    def append_right(self, element):
        if self.buffer_left + self.length >= len(self.array):
            self.expand_right()
        self.array[self.buffer_left + self.length] = element
        self.length += 1

    def append_left(self, element):
        if self.buffer_left == 0:
            self.expand_left()
        self.array[self.buffer_left -1] = element
        self.length += 1
        self.buffer_left -= 1

    def expand_right(self, new_size = None):
        if new_size is None:
            new_size = len(self.array)*2
        new_array = np.zeros(new_size, dtype = object)
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        self.array = new_array

    def expand_left(self, new_size = None):
        if new_size is None:
            new_size = len(self.array)*2
        self.buffer_left = len(self.array)
        new_array = np.zeros(new_size, dtype = object)
        for i in range(len(self.array)):
            new_array[self.buffer_left + i] = self.array[i]
        self.array = new_array

    def pop_left(self):
        self.array[self.buffer_left] = 0
        self.buffer_left += 1
        self.length -= 1

    def pop_right(self):
        self.array[self.buffer_left + self.length -1] = 0
        self.length -= 1

    def get(self, index):
        print(self.array[self.buffer_left + index])

    def insert(self, index, element):
        self.array[self.buffer_left + index] = element

if __name__ == "__main__":
    list = ArrayList(4)
    
    list.append_left(1)
    list.append_left(2)
    list.append_left(3)
    list.append_left(4)
    
    print(list.array)
    list.pop_right()
    print(list.array)
    list.insert(0, 1)
    print(list.array)
    list.get(0)
    
    

    
