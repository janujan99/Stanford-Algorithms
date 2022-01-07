class MinHeap:
    def __init__(self, lst=[]) -> None:
        self.lst = lst
        self.length = len(lst)

    def getParentIndex(self, index):
        return max(0,(index-2)//2)

    def getLeftChildIndex(self, index):
        if index*2 + 1 >= self.length:
            return None
        return index*2 + 1
    
    def getRightChildIndex(self, index):
        if index*2 + 2 >= self.length:
            return None
        return index*2 + 2

    def swap(self, index1, index2):
        temp = self.lst[index2]
        self.lst[index2] = self.lst[index1]
        self.lst[index1] = temp
        return

    def heapifyUp(self):
        index = self.length - 1
        while (index > 0 and self.lst[self.getParentIndex(index)] > self.lst[index]):
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)
        return

    def heapifyDown(self):
        index = 0 
        
        while self.getLeftChildIndex(index):
            new_index = self.getLeftChildIndex(index)
            if self.getRightChildIndex(index) and self.lst[self.getRightChildIndex(index)]<self.lst[new_index]:
                new_index = self.getRightChildIndex(index)
            if self.lst[index] > self.lst[new_index]:
                self.swap(index, new_index)
                index = new_index
            else:
                break 
        return

    def add(self, item):
        self.lst.append(item)
        self.length += 1
        self.heapifyUp()
        return

    def extract_min(self):
        minimum = self.lst[0]
        self.lst[0] = self.lst[self.length-1]
        self.lst = self.lst[:-1]
        self.length += -1
        self.heapifyDown()
        return minimum
    
            


heap = MinHeap([3,4,8,9,7,10,9,15,20,13])

mine = heap.extract_min()

print("Minimum: " + str(mine))
print(heap.lst)