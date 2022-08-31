from re import S
import numpy as np

class ArrayList:
    def __init__(self, startcapasity = 20):
        self.array = np.zeros(startcapasity, dtype=object)
        self.length = 0
        self.startIndex = 0

    def __len__(self):
        return self.length
    
    def expand_left(self, new_size=None):
        #if no new size is specified, double the array size
        if new_size is None:
            new_size = len(self.array)*2
        
        #initialize new array with zeros.
        new_array = np.zeros(new_size, dtype = object)
        
        #copy over all the elements from the old array
        #into the new one
        #we want the buffer to be on the "left" side of the array
        old_array_len = len(self.array)
        for i in range(old_array_len):
            new_array[i+old_array_len] = self.array[i]
        
        #set the new array to be the current array
        self.array = new_array
        self.startIndex += 1
    
    def expand_right(self, new_size = None):
        if new_size is None:
            new_size = len(self.array)*2
        
        new_array = np.zeros(new_size, dtype = object)

        old_array_len = len(self.array)
        for i in range(old_array_len):
            new_array

    def append_left(self, element):
        if self.length >= len(self.array):
            self.expand_left()
        
        if self.length == 0:
            self.array[-1] = element
        else:
            self.array[-(self.length+1)] = element
        self.length += 1
    
      
        
        

if __name__ == "__main__":
    list = ArrayList(2)
    print("length: ", list.length)
    
    
    list.append_left(1)
    list.append_left(2)
    list.append_left(3)
    list.append_left(4)
    list.append_left(5)
    
    print(list.array)
