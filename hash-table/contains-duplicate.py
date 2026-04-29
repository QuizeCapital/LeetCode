class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # for i,num in enumerate(nums):
        #     for j,duplicate in enumerate(nums):
        #         if num == duplicate and i != j:
        #             return True 
        # return False

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


