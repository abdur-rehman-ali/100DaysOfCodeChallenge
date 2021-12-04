import math
def mergeSort(A,low,high):
    if low<high:
        mid = math.floor((low+high) / 2)
        mergeSort(A,low,mid)
        mergeSort(A,mid+1,high)
        merge(A,low,mid,high)
        
    

def merge(A,low,mid,high):
    i=low
    j=mid+low
    C = []
    while (i<mid and j<high):
        if A[i] < A[j]:
            C.append(A[i])
            i+=1
        else:
            C.append(A[j])
            j+=1

    if i<mid:
        while(i<mid):
            C.append(A[i])
            i+=1
    else:
        while(j<high):
            C.append(A[j])
            j+=1
        

# A = [1,2,3,4,43,2,432,23,43,5,6,7,8,9,11,12,13,112,223,333,444]


