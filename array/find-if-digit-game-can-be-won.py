class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        return sum(i for i in nums if i >= 10) != sum(i for i in nums if i <= 9)
        