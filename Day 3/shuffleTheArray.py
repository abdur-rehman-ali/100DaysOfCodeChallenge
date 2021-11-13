def shuffle( nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        # for index,value in enumerate(nums):
        #     print(f"index = {index} , value = {value}")
        shuffled_array = []
        ind=0
        for i in range(0,2*n,2):
                shuffled_array.insert(i,nums[i])
                shuffled_array.insert(i+1,nums[ind+n])
                ind+=1
        return shuffled_array

nums = [1,2,3,4,5,6]
n=3
print(shuffle(nums, n))
