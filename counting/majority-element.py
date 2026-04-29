class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_data = {i:0 for i in nums}
        for i in nums: 
            dict_data[i] += 1
        
        # for key,value in dict_data.items():
        
        return max(dict_data, key = dict_data.get)

print(Solution().majorityElement([2,2,1,1,1,2,2]))