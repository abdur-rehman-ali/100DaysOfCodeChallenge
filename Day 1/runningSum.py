
def runningSum(nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        """
        runningSumList = []
        for key,value in enumerate(nums):
            sum = 0
            for i in range(0,key+1):
                sum = sum + nums[i]
            runningSumList.append(sum)
        return runningSumList


def runningSumEffective(nums):
       runningSumList = []
       runningSumList.append(nums[0])
       for key in range(1,len(nums)):
           runningSumList.append(runningSumList[key-1] + nums[key])
       return runningSumList

nums = [1,2,3,4,5]

print(runningSumEffective(nums))
