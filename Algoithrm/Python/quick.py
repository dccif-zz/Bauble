import time


def exchange(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if (arr[j] <= x):
            i = i + 1
            exchange(arr, i, j)
    exchange(arr, i + 1, r)
    return i + 1


def quickSort(arr, p, r):
    if (p < r):
        q = partition(arr, p, r)
        quickSort(arr, p, q - 1)
        quickSort(arr, q + 1, r)


arr = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
print(arr)
start = time.clock()
times = 100000
for i in range(0, times):
    quickSort(arr, 0, arr.__len__() - 1)
end = time.clock()
print(arr)
print((end - start) / times)
