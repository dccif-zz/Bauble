S=[97,1,88,5,3,345,23,664]

def mergeSort(s):
    if len(s)<=1:
        return s
    mid = int(len(s)/2)
    left = mergeSort(s[:mid])
    right = mergeSort(s[mid:])
    return merge(left,right)

def merge(left,right):
    result=1
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result=result+1
            i+=1
        else:
            j+=1
            
    return result

    
    
    
