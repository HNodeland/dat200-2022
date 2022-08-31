from re import S
import numpy as np

class ArrayListe:
    def __init__(self, startcapasity = 20):
        self.array = np.zeros(startcapasity, dtype=object)
        self.length = 0
        