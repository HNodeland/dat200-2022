from re import S
from tracemalloc import start
import numpy as np

class ArrayList:
    def __init__(self, startcapasity = 20):
        self.array = np.zeros(startcapasity, dtype=object)
        self.length = 0
        self.buffer_left = int(startcapasity/2)

    #Kjøretid O(1)
    def __len__(self):
        return self.length
    
    #Kjøretid best case O(1)
    #Kjøretid worst case O(n), når lista må utvides, og alle elementer må flyttes
    #Kjøretid amortized O(1)
    def append_right(self, element):
        if self.buffer_left + self.length >= len(self.array):
            self.expand_right()
        self.array[self.buffer_left + self.length] = element
        self.length += 1

    #Kjøretid best case O(1)
    #Kjøretid worst case O(n), når lista må utvides, og alle elementer må flyttes
    #Kjøretid amortized O(1)
    def append_left(self, element):
        if self.buffer_left == 0:
            self.expand_left()
        self.array[self.buffer_left -1] = element
        self.length += 1
        self.buffer_left -= 1

    #Kjøretid O(n)
    def expand_right(self, new_size = None):
        if new_size is None:
            new_size = len(self.array)*2
        new_array = np.zeros(new_size, dtype = object)
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        self.array = new_array

    #Kjøretid O(n)
    def expand_left(self, new_size = None):
        if new_size is None:
            new_size = len(self.array)*2
        self.buffer_left = len(self.array)
        new_array = np.zeros(new_size, dtype = object)
        for i in range(len(self.array)):
            new_array[self.buffer_left + i] = self.array[i]
        self.array = new_array

    #Kjøretid O(1)
    def pop_left(self):
        self.array[self.buffer_left] = 0
        self.buffer_left += 1
        self.length -= 1

    #Kjøretid O(1)
    def pop_right(self):
        self.array[self.buffer_left + self.length -1] = 0
        self.length -= 1

    #Kjøretid O(1) best case, rett på første element i lista
    #Kjøretid O(n) worst case, når vi leter gjennom hele arrayet 
    def get(self, index):
        print(self.array[self.buffer_left + index])

    #Kjøretid O(1) best case, rett på første element i lista
    #Kjøretid O(n) worst case, når vi leter gjennom hele arrayet 
    def replace(self, index, element):
        self.array[self.buffer_left + index] = element
    
    #Kjøretid O(1) best case, elementet plasseres på slutten av arrayet 
    #Kjøretid O(n) worst case, på starten av arrayet, og alle elementene må flyttes
    def insert(self, index, element):
        if self.buffer_left + self.length >= len(self.array):
            self.expand_right()
        for i in range(self.length -1, index -1, -1):
            self.array[self.buffer_left + i + 1] = self.array[self.buffer_left + i]
        self.array[self.buffer_left + index] = element
        self.length += 1
        

if __name__ == "__main__":
    list = ArrayList(4)
    
    list.append_right(1)
    list.append_right(2)
    list.append_right(3)
    list.append_right(4)
    list.append_left(1)
    list.append_left(2)
    list.append_left(3)
    print(list.array)
    
