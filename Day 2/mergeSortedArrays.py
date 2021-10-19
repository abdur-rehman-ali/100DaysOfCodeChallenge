
def merge( nums1, m, nums2, n):
    merged_array = []
    i=0
    j=0
    while i<m and j <n:
        if nums1[i] < nums2[j]:
            merged_array.append(nums1[i])
            i+=1
        else:
            merged_array.append(nums2[j])
            j+=1
    for k in range(i,m):
            merged_array.append(nums1[k])

    for k in range(j,n):
            merged_array.append(nums2[k])

    return merged_array

nums1 = [1,2,3,4,5,6,7]
nums2 = [2,5,6,7,8,9,12]
nums1.sort()
nums1.sort()

print(merge(nums1,len(nums1),nums2,len(nums2)))