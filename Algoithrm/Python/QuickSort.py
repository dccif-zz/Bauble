import time


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


start = time.clock()
print(quicksort([2, 8, 7, 1, 3, 5, 6, 4, 9, 10]))
ends = time.clock()
print(str(ends - start))
