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


def RSelect(A, l, r, i) -> None:
    if r-l == 0:
        return A[0]

    j = partition(A, l, r)
    if i == j:
        return A[j]

    elif i < j:
        return RSelect(A, l, j, i)
    else:
        return RSelect(A, j + 1, r, i-j)

def randomized_select(A, i):
    return RSelect(A, 0, len(arr), i-1)

arr = [5,1,2,3]
print(randomized_select(arr, 3))
