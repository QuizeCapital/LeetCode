class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        total = 0
        for i in nums:
            if i % 6 == 0:
                total += i
                count += 1
        if count == 0 :
            return 0
        return total // count
        