def countingSort(A):
    length = A.__len__()
    C = [0] * A.__len__()
    B = [0] * A.__len__()
    for j in range(0, length):
        C[A[j]] = C[A[j]] + 1
    for i in range(1, length):
        C[i] = C[i] + C[i - 1]
    for j in range(length - 1, 0, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1
    return B


A = [2, 5, 3, 0, 2, 3, 0, 3, 4, 6, 7, 9]

print(countingSort(A))
