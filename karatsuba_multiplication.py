import math
import testing_helpers
import time
import pandas as pd

def multiply_one_digit(n1: list, n2: list):
    prod = n1[0] * n2[0]
    carryover = prod // 10
    if carryover > 0:
        return [carryover, prod % 10]
    return [prod]

def sum_lists(arr_lst):
    summation = [0]*len(arr_lst[0])
    carryover = 0
    for x in range(len(arr_lst[0])-1, -1, -1):
        full_num = sum([lst[x] for lst in arr_lst]) + carryover
        summation[x] = full_num % 10
        carryover = full_num // 10

    if not all(summation):
        return summation
    index = 0
    while(summation[index] == 0):
        index += 1

    return summation[index:]


def sum_uneven_length(arr_lst: list):
    sum_length = max([len(x) for x in arr_lst]) + 1

    new_arr_lst = []

    for arr in arr_lst:
        missing_zeroes = sum_length - len(arr)
        new_arr = [x for x in arr]
        for x in range(missing_zeroes):
            new_arr.insert(0, 0)
        new_arr_lst.append(new_arr)

    return sum_lists(new_arr_lst)


def multiply(n1: list, n2: list) -> list:
    assert len(n1) == len(n2)
    if len(n1) == 1:
        return multiply_one_digit(n1, n2)
    # split the arrays
    split = len(n1)//2
    a = n1[:split]
    b = n1[split:]
    c = n2[:split]
    d = n2[split:]

    n = len(n1)

    s1 = multiply(a, c)+([0]*n)
    s2 = sum_uneven_length([multiply(a, d), multiply(b, c)])+([0]*(n//2))
    s3 = multiply(b, d)

    return sum_uneven_length([s1, s2, s3])


def closest_greater_pow_of_two(n):
    for x in range(n):
        if 2**x >= n:
            return 2**x


def karatsuba_multiply(n1, n2):
    closest_pow = closest_greater_pow_of_two(len(n1))
    for x in range(closest_pow - len(n1)):
        n1.insert(0, 0)
        n2.insert(0, 0)

    return multiply(n1, n2)


# print(multiply_one_digit([5],[6]))
# print(get_tenth_power(2,[5]))
#print(sum_uneven_length([[5,0,0], [1,6,0], [1,2]]))
#print(karatsuba_multiply([5, 6, 7, 8], [1, 2, 3, 4]))
powers_of_two = [2**x for x in range(15)]

times = []
index = []
df = pd.DataFrame()

for x, length in enumerate(powers_of_two):
    arr1 = testing_helpers.generate_random_arrays(length)
    arr2 = testing_helpers.generate_random_arrays(length)
    initial = time.time()
    karatsuba_multiply(arr1, arr2)
    final = time.time()
    times.append(final-initial)
    print(f"{length}: {times[-1]}")

df['Length'] = powers_of_two
df['Time (s)'] = times

df.to_csv(path_or_buf="./times_katsuba.csv", index=False)