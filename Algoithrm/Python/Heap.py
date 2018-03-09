def parent(i):
    return i // 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def exchange(Arr, i, largest):
    temp = Arr[i]
    Arr[i] = Arr[largest]
    Arr[largest] = temp


def maxHeapify(Arr, i):
    l = left(i)
    r = right(i)
    if (l <= Arr.__len__() - 1 and Arr[l] > Arr[i]):
        largest = l
    else:
        largest = i
    if (r <= Arr.__len__() - 1 and Arr[r] > Arr[largest]):
        largest = r
    if largest != i:
        exchange(Arr, i, largest)
        maxHeapify(Arr, largest)


def buildMaxHeap(Arr):
    length = (Arr.__len__() - 1) // 2
    for i in list(range(length, 0, -1)):
        maxHeapify(Arr, i)


if __name__ == "__main__":
    Arr = [0, 16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    print("Before: " + str(Arr[1:]))
    buildMaxHeap(Arr)
    print("After: " + str(Arr[1:]))
