

def maximumSubArraySum(nums):
    """
    Brute force appraoch with time complexity = O(n^3)
    """
    max_sum=nums[0]
    for i in range(len(nums)):
       for j in range(len(nums)):
           subArray_sum = 0
           for k in range(i,j+1):
               subArray_sum = subArray_sum + nums[k]
               if subArray_sum >max_sum:
                   max_sum = subArray_sum

    return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
