class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(sorted(nums))
        print(range(0,len(nums)))
        unique = set(range(0,len(nums)+1)) - set(nums)
        print(unique)
        # for i in range(0,len(nums)+1):
        #     # print(i)
        #     if  i not in sorted(nums): 
        #         return i
        return unique.pop()
        
print(Solution().missingNumber([0,1]))
