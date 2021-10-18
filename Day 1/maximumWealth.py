def maximumWealth(accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        
        Time complexity = O(n)
        Brute force appraoch
        """
        all_sum = []
        for row,row_value in enumerate(accounts):
            sum = 0
            for col,col_value in enumerate(row_value):
                sum = sum + col_value
            all_sum.append(sum)
        return max(all_sum)

accounts = [[1,2,3],[3,2,1]]
print(maximumWealth(accounts))