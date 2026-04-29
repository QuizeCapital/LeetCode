class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict_n = {i : 0 for i in nums}
        res = []
        for i in nums: 
            if i in dict_n:
                dict_n[i] += 1
        for k,v in dict_n.items():
            if v>1:
                res.append(k)
        return res 
        