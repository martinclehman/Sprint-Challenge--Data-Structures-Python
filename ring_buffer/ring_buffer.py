class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity

        # Use a list to store ring
        self.list = [None] * capacity
        self.ring_index = 0

    def append(self, item):

        # store values into ring array until you hit the end, and 
        # start the ring index back at 0
        if self.ring_index < self.capacity:
            self.list[self.ring_index] = item
            self.ring_index += 1
        else:
            self.list[0] = item
            self.ring_index = 1
            
    def get(self):

        # print a list with values if array is filled
        output = []
        for element in self.list:
            if element:
                output.append(element)
        return output
        