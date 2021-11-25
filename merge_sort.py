def merge(arr1, arr2):
    p1 = 0
    p2 = 0
    new = []
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] > arr2[p2]:
            new.append(arr2[p2])
            p2 += 1
        else:
            new.append(arr1[p1])
            p1 += 1
    if p1 == len(arr1):
        new.extend(arr2[p2:])
    else:
        new.extend(arr1[p1:])
    return new


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    elif len(arr) == 2:
        if arr[1] > arr[0]:
            return arr
        else:
            return [arr[1], arr[0]]
    split = len(arr) // 2
    return merge(merge_sort(arr[:split]), merge_sort(arr[split:]))
