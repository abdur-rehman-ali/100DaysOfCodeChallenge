
def majorityElementOptimal(nums):
    hash_map={}
    """
    Time compelexity = O(n)
    Space compelexity = O(n)
    """
    #This loop will store frequency of each element in nums
    for i in nums:
        if i in hash_map.keys():
            hash_map[i] = hash_map[i] + 1
        else:
            hash_map[i] = 1

    max_count = 0
    max_value = -1
    for key in hash_map.keys():
        if hash_map[key] > max_count:
            max_count = hash_map[key]
            max_value = key
       
    if max_count > len(nums) / 2:
        return max_value
    else:
        return -1
        

nums = [1,2,3,1,1,1,1,1,1,3,3,4]
print(majorityElementOptimal(nums))