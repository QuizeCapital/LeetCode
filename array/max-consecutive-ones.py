class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ro_indices = [0]
        max_num = 0
        for ind, i in enumerate(nums):
            if i == 0:
                ro_indices.append(ind)
        ro_indices.append(len(nums))
        for i in range(len(ro_indices)-1):
            if i == 0 and abs(ro_indices[i+1] - ro_indices[i]) > max_num:
                max_num = abs(ro_indices[i+1] - ro_indices[i])
            if abs(ro_indices[i+1] - ro_indices[i]) > max_num:
                max_num = abs(ro_indices[i+1] - ro_indices[i])-1
        return max_num

