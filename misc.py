import random

def first_nonzero_index(lst):
    for index, element in enumerate(lst):
        if element != 0:
            return index
    return -1

def timeVariance():
    return random.uniform(0.1, 0.3)