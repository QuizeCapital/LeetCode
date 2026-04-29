class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        first, last = 0, n-1
        while first <= last:

            mid =  ((first + last) // 2) 
            if mid < n-1 and nums[mid] < nums[mid+1]:
                first = mid+1
            elif mid > 0 and nums[mid] < nums[mid-1]:
                last = mid-1
            else:
                return mid 

# class Solution:
#     def findPeakElement(self, nums):
#         n = len(nums)
#         low, high = 0, n-1
#         while low <= high:
#             mid = ((high-low)//2) + low
#             # Peak element is present in right side
#             if mid < n-1 and nums[mid] < nums[mid+1]:
#                 low = mid+1
#             # Peak element is present in left side
#             elif mid > 0 and nums[mid] < nums[mid-1]:
#                 high = mid-1
#             else:
#                 return mid     


        