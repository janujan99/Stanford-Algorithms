import time
import random
import math
import testing_helpers
import pandas as pd


def multiply_small(n1: list, num: int):
    product = [0]*(len(n1) + 1)
    carryover = 0
    for x in range(len(n1)-1, -1, -1):
        full_num = n1[x] * num + carryover
        product[x+1] = full_num % 10
        carryover = full_num // 10
    product[0] = carryover
    return product


def sum_lists(arr_lst):
    summation = [0]*len(arr_lst[0])
    carryover = 0
    for x in range(len(arr_lst[0])-1, -1, -1):
        full_num = sum([lst[x] for lst in arr_lst]) + carryover
        summation[x] = full_num % 10
        carryover = full_num // 10

    index = 0
    while(summation[index] == 0):
        index += 1

    return summation[index:]


def multiply(n1, n2):
    product = []
    for x in range(len(n2)-1, -1, -1):
        arr = multiply_small(n1, n2[x])
        for y in range(len(n2)-1-x):
            arr.append(0)
        product.append(arr)

    final_length = 2*len(n1)+1
    refined_product = []
    for arr in product:
        refined_product.append([0]*(final_length-len(arr)) + arr)
    return sum_lists(refined_product)

#assert(multiply([5,6,7,8], [1,2,3,4])) == [7,0,0,6,6,5,2]
#assert(multiply([9,9,9,9,9,9],[9,9,9,9,9,9])) == [9,9,9,9,9,8,0,0,0,0,0,1]
powers_of_two = [2**x for x in range(15)]

times = []
index = []
df = pd.DataFrame()

for x, length in enumerate(powers_of_two):
    arr1 = testing_helpers.generate_random_arrays(length)
    arr2 = testing_helpers.generate_random_arrays(length)
    initial = time.time()
    multiply(arr1, arr2)
    final = time.time()
    times.append(final-initial)
    print(f"{length}: {times[-1]}")

df['Length'] = powers_of_two
df['Time (s)'] = times

df.to_csv(path_or_buf="./times_normal.csv", index=False)
