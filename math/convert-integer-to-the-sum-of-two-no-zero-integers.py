class Solution(object):
    # def getNoZeroIntegers(self, n):
    #     for i in range(1, n):
    #         j = n - i
    #         if '0' not in str(i) and '0' not in str(j):
    #             return [i, j]
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(1,n):
            j = n-i
            if '0' not in str(i) and '0' not in str(j):
                return [i, j]
                # break 
        
        # return False


print(Solution().getNoZeroIntegers(11))