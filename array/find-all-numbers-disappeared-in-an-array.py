class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        full_list = [i for i in range(1,len(nums)+1)]
        trunc_list = set(nums)

        return list(set(full_list)- (trunc_list))
print(Solution().findDisappearedNumbers([1,1]))