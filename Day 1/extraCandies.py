def kidsWithCandies(candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result=[]
        max_count=max(candies)
        print(max_count)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_count:
                result.append(True)
            else:
                result.append(False)
        return result

candies = [2,3,5,1,3]
print(kidsWithCandies(candies,3))