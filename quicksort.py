def partition(A, l, r) -> int:
    pivot = A[l]
    i = l+1

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


def quicksort(A, l, r) -> None:
    if r-l in [0, 1]:
        return

    pivot_location = partition(A, l, r)

    quicksort(A, l, pivot_location)
    quicksort(A, pivot_location + 1, r)
    return

# partition(arr, 0, 6)
# arr = [2,1,3,4,9,5]
# pivot_location = 2
# quicksort(arr, 0, 2)
    # partition(arr, 0, 2)
    # arr = [1,2,3,4,9,5]
    # pivot_location =  1
    # quicksort(arr, 0, 1)
    # return
    # quicksort(arr, 2, 2)


arr = [3, 1, 4, 2, 5, 9]


quicksort(arr, 0, len(arr))
print(arr)
# prove that A[0:j] is partitioned correctly on jth iteration
# prove partition works for array A
# pivot  = A[0]
# i: index such that i <= j, where all elements in A[1..i] are less than the pivot, but A[i] is > pivot
# j: index such that A[1..j] is partitioned, and A[j...] is unpartitioned
# Base case: i = j = 1 -> A[1..i] is null , and A[1..j] is partitioned since it is null, and A[j...] is unpartitioned as it has not been scanned. So BC is valid.
# Assume that for array A, A[1:j] is partitioned correctly on jth iteration, and i is in the correct position.
# If A[j+1] > pivot do nothing, as (j+1)th element is in correct spot by definition
# Otherwise, swap A[i] and A[j+1], then increment i by 1. This means that the element that used to be at position j+1 is now in position i, a


