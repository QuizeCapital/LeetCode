class Solution(object):
    import math
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val = 1
        for i in nums:
            val *= i
        
        if val == 0:
            return 0
        elif val < 0:
            return -1
        else:
            return 1

    

        