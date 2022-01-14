class MinHeap:
    def __init__(self, lst=[]) -> None:
        self.lst = []
        for num in lst:
            self.add(num)
        

    def getParentIndex(self, index):
        assert index > 0
        return (index-1)//2

    def getLeftChildIndex(self, index):
        if index*2 + 1 >= len(self.lst):
            return None
        return index*2 + 1

    def getRightChildIndex(self, index):
        if index*2 + 2 >= len(self.lst):
            return None
        return index*2 + 2

    def swap(self, index1, index2):
        temp = self.lst[index2]
        self.lst[index2] = self.lst[index1]
        self.lst[index1] = temp
        return

    def heapifyUp(self):
        index = len(self.lst) - 1
        while (index > 0 and self.lst[self.getParentIndex(index)] > self.lst[index]):
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)
        return

    def heapifyDown(self, root):
        left = self.getLeftChildIndex(root)
        right = self.getRightChildIndex(root)

        if left is None:
            return
        
        if right is None:
            if self.lst[root] > self.lst[left]:
                self.swap(root, left)
                self.heapifyDown(left) 
            else:
                return
        
        else:
            lesser_element_index = left if self.lst[left] < self.lst[right] else right
            if self.lst[root] < self.lst[lesser_element_index]:
                return  
            else:
                self.swap(root, lesser_element_index)
                self.heapifyDown(lesser_element_index)
        return 
        



    def add(self, item):
        self.lst.append(item)
        self.heapifyUp()
        return

    def extract_min(self):
        if len(self.lst) == 0:
            return None
        minimum = self.lst[0]
        self.lst[0] = self.lst[len(self.lst)-1]
        self.lst = self.lst[:-1]
        self.heapifyDown(0)
        return minimum

    def peek_min(self):
        if len(self.lst) == 0:
            return None
        return self.lst[0]

    def get_length(self):
        return len(self.lst)

import random

nums = [random.randint(0,100000) for x in range(100)]

heap = MinHeap(nums)

length = heap.get_length()

result = [heap.extract_min() for x in range(length)]
expected = sorted(nums)

for i in range(len(result)):
    print(result[i], expected[i])
    assert result[i] == expected[i]

