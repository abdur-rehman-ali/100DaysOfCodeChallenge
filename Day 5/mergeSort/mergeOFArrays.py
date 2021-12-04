

def merge(A,B,m,n):
    i=0
    j=0
    C = []
    while (i<m and j<n):
        if A[i] < B[j]:
            C.append(A[i])
            i+=1
        else:
            C.append(B[j])
            j+=1

    if i<m:
        while(i<m):
            C.append(A[i])
            i+=1
    else:
        while(j<n):
            C.append(B[j])
            j+=1
        
    print(C)

A = [1,2,3,4,5,6,7,8,9,11,12,13,112,223,333,444]
B = [5,6,7,8,9]
merge(A,B,len(A),len(B))