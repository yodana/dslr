import statistics
from math import *

class Encoder(object):
    def __init__(self, data):
        self.data = sorted(data)
        self.median = statistics.median(self.data)
        self.irq = self.get_q3(self.data) - self.get_q1(self.data)

    def get_q1(self, data):
        ret = data[ceil(len(data) / 4) - 1]
        return ret
    
    def get_q3(self, data):
        ret = data[ceil(3 * len(data) / 4) - 1]
        return ret

    def normalize(self, data):
        ret = []
        for x in data:
            ret.append(float((x - self.median) / self.irq))
        return ret

    def denormalize(self, data):
        ret = []
        for x in data:
            ret.append(x * self.irq + self.median)
        return ret

    def denormalize_one(self, data):
        return data * self.irq + self.median
        