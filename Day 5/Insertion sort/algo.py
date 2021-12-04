def insertionSort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i-1
        while(arr[j]>temp and j>=0):
            arr[j+1]=arr[j]
            j -=1
        arr[j+1]=temp
    print(arr)


arr = [2,3,5,4,9,8,7]
insertionSort(arr)