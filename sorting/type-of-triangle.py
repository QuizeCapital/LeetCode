class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not (nums[0] + nums[1] > nums[2] and nums[0] + nums[2] > nums[1] and nums[2] + nums[1] > nums[0]):
            return "none" 
        if len(set(nums)) == 1:
            return 'equilateral'
        elif len(set(nums)) ==2:
            return 'isosceles'
        elif len(set(nums)) ==3:
            return 'scalene'
        
        