
"""
Return element which exist more than N/2 times in array
And return -1 if no majority element exist
"""
def majorityElement(nums):
    """
    Brute force approach with time complexity = O(n^2)
    """
    
    max_count = 0
    
    for i in range(len(nums)):
        count=0
        for j in range(len(nums)):
            if nums[j] == nums[i]:
                count = count + 1

        if count > max_count:
            max_count = count
            max_index = i
        
    if max_count > (len(nums) / 2 ):
        return nums[max_index]
    else:
        return -1

nums = [1,2,3,1,1,1,1,1,1,3,3,4]
print(majorityElement(nums))