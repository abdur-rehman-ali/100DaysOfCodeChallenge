
def insertionSort(nums):
    """
    type nums : List(int)
    rtype: List(int)
    """
    for i in range(1,len(nums)):
        for j in range(0,i+1):
            if nums[j] > nums[i]:
                dummy = nums[j]
                nums[j] = nums[i]
                nums[i] = dummy
    return nums


nums = [8,7,5,2,4,6,3]
print(insertionSort(nums))