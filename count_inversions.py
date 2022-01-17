from typing import List, Tuple
import read_text_into_array

def merge_and_count_split_inversions(arr1, arr2):
    inversions = 0
    p1 = 0
    p2 = 0
    new = []
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] > arr2[p2]:
            new.append(arr2[p2])
            p2 += 1
            inversions += len(arr1)-p1
        else:
            new.append(arr1[p1])
            p1 += 1
    if p1 == len(arr1):
        new.extend(arr2[p2:])
    else:
        new.extend(arr1[p1:])

    return new, inversions


def sort_and_count_inversions(arr) -> Tuple[List[int], int]:
    if len(arr) == 0 or len(arr) == 1:
        return arr, 0
    split = len(arr) // 2

    B, x = sort_and_count_inversions(arr[:split])
    C, y = sort_and_count_inversions(arr[split:])
    D, z = merge_and_count_split_inversions(B, C)

    return D, x+y+z


print(sort_and_count_inversions(read_text_into_array.read_array("/Users/janujansritharan/Desktop/Resumes/IntegerArray.txt")))
