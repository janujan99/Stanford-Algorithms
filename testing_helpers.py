import random

def generate_random_arrays(length):
    arr1 = []
    for i in range(length):
        arr1.append(random.randint(1, 9))
    return arr1

