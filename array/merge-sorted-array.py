class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        last_num1 = m - 1     
        last_num2 = n - 1      
        insert_position = m + n - 1  

        while last_num2 >= 0:
            if last_num1 >= 0 and nums1[last_num1] > nums2[last_num2]:
                nums1[insert_position] = nums1[last_num1]
                last_num1 -= 1
            
            else: 
                nums1[insert_position] = nums2[last_num2]
                last_num2 -= 1

            insert_position -= 1

print(Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
        