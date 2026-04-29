class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Missing number
        missing = list(set(range(1, len(nums)+1)) - set(nums))[0]

        # Duplicate = sum(nums) - sum(set(nums))
        duplicate = sum(nums) - sum(set(nums))

        return [duplicate, missing]

print(Solution().findErrorNums([1,2,2,4]))