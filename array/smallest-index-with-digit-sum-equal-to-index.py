class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for enum, val in enumerate(nums):
            sum_val = sum(int(i) for i in list(str(val)))
            if enum == sum_val:
                return enum
        return -1
        