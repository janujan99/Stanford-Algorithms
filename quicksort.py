import read_text_into_array

def get_median(A, l, r):
    arr = [l, (l+r-1)//2, r-1]
    print(arr)
    arr_max = max([A[x] for x in arr])
    arr_min = min([A[x] for x in arr])
    index = None
    for x in arr:
        if not A[x] in [arr_max, arr_min]:
            index = x
    return index


def partition(A, l, r) -> int:
    if r-l == 1:
        return 0
    elif r-l == 0:
        return 0
    index = get_median(A, l, r)
    
    temp = A[l]
    A[l] = A[index]
    A[index] = temp
    
    pivot = A[l]
    i = l+1
    global counter
    for j in range(l+1, r):
        if A[j] < pivot:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i += 1
    
    temp = A[i-1]
    A[i-1] = A[l]
    A[l] = temp
    return i-1

comparisons = 0

def quick_sort(A, l, r) -> None:
    if r-l in [0, 1]:
        return

    pivot_location = partition(A, l, r)

    global comparisons 
    comparisons += max(0, pivot_location-l-1)
    comparisons += max(0, r-pivot_location-2)
    quick_sort(A, l, pivot_location)
    quick_sort(A, pivot_location + 1, r)
    return


arr = read_text_into_array.read_array("/Users/janujansritharan/Desktop/Resumes/QuickSort.txt")
quick_sort(arr, 0, len(arr))
print(comparisons+len(arr)-1)
# prove that A[0:j] is partitioned correctly on jth iteration
# prove partition works for array A
# pivot  = A[0]
# i: index such that i <= j, where all elements in A[1..i] are less than the pivot, but A[i] is > pivot
# j: index such that A[1..j] is partitioned, and A[j...] is unpartitioned
# Base case: i = j = 1 -> A[1..i] is null , and A[1..j] is partitioned since it is null, and A[j...] is unpartitioned as it has not been scanned. So BC is valid.
# Assume that for array A, A[1:j] is partitioned correctly on jth iteration, and i is in the correct position.
# If A[j+1] > pivot do nothing, as (j+1)th element is in correct spot by definition
# Otherwise, swap A[i] and A[j+1], then increment i by 1. This means that the element that used to be at position j+1 is now in position i, a


#print(get_median([8,2,4,5,7,1], 0, 6))