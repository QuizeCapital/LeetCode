class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for ind,  value in enumerate(nums):
            for ind_, value_ in enumerate(nums):
                print(ind_, ind, value_, value)
                if nums[ind] == nums[ind_] and ind < ind_ :
                    res_tuple = (ind, ind_)
                    res.append(res_tuple)
        return len(res) 
        