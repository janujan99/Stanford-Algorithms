from minHeap import MinHeap

class MaxHeap:
    def __init__(self, lst=[]):
        self.minHeap = MinHeap([num*(-1) for num in lst])
    
    def add(self, item):
        self.minHeap.add(item*(-1))
        return
    
    def extract_max(self):
        return self.minHeap.extract_min()*(-1)

    def peek_max(self):
        return self.minHeap.peek_min()*(-1)  
    
    def get_length(self):
        return self.minHeap.get_length()
    
    
