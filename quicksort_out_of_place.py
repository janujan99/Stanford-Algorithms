from typing import List, Tuple


def partition(A) -> Tuple[List, List]:
    pivot = A[0]
    less_than = []
    greater_than = []

    for x in range(1, len(A)):
        if A[x] < pivot:
            less_than.append(A[x])
        else:
            greater_than.append(A[x])

    return less_than, greater_than


def quicksort(A) -> List:
    if len(A) == 1 or len(A) == 0:
        return A

    l, r = partition(A)

    return quicksort(l) + [A[0]] + quicksort(r)


arr = [3, 1, 4, 2, 5, 9]

print(quicksort(arr))
# prove that A[0:j] is partitioned correctly on jth iteration
# prove partition works for array A
# pivot  = A[0]
# i: index such that i <= j, where all elements in A[1..i] are less than the pivot, but A[i] is > pivot
# j: index such that A[1..j] is partitioned, and A[j...] is unpartitioned
# Base case: i = j = 1 -> A[1..i] is null , and A[1..j] is partitioned since it is null, and A[j...] is unpartitioned as it has not been scanned. So BC is valid.
# Assume that for array A, A[1:j] is partitioned correctly on jth iteration, and i is in the correct position.
# If A[j+1] > pivot do nothing, as (j+1)th element is in correct spot by definition
# Otherwise, swap A[i] and A[j+1], then increment i by 1. This means that the element that used to be at position j+1 is now in position i, a
