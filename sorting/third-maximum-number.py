class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = sorted(set(nums))
        # if len(nums)<=2 and len(nums) > 1:
        #     return nums[-1]
        # return nums[-2]
        if len(set(nums)) >= 3:
            return sorted(set(nums))[-3]
        else:
            return sorted(set(nums))[-1]
print(Solution().thirdMax([1,1,1]))