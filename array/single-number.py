class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # set_one = set([4,1,2,1,2])
        # for num in nums: 
        #     if num not in set_one:
        #         set_one.add(num)
        # for i in range(len(sorted(nums))):
        #     if nums[i] != 
        dict_data = {i:0 for i in set(nums)}
        for i in nums:
            dict_data[i] += 1

        return min(dict_data, key = dict_data.get)
    
print(Solution().singleNumber( [2,2,1]))
        