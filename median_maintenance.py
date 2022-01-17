from minHeap import MinHeap
from maxHeap import MaxHeap

def get_median_sum(lst):
    curr_med = None
    med_sum = 0
    hHigh = MinHeap()
    hLow = MaxHeap()

    for i,num in enumerate(lst):
        if i == 0:
            hLow.add(num)
        elif num < hLow.peek_max():
            hLow.add(num)
        else:
            hHigh.add(num)
        
        if hLow.get_length() - hHigh.get_length() == 2:
            hHigh.add(hLow.extract_max())
        elif hHigh.get_length() - hLow.get_length() == 2:
            hLow.add(hHigh.extract_min())

        if hLow.get_length() < hHigh.get_length():
            curr_med = hHigh.peek_min()
        elif hLow.get_length() >= hHigh.get_length():
            curr_med = hLow.peek_max()

        med_sum += curr_med

    return med_sum

lines = open("Median.txt", "r").readlines()
nums = [int(line[:-1]) for line in lines]
print(get_median_sum(nums)%10000)





