class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
    #     class Solution:
    # def mySqrt(self, x: int) -> int:
        # if x == 0:
        #     return 0
        
        # left, right = 1, x
        # result = 0
        
        # while left <= right:
        #     mid = (left + right) // 2
        #     mid_squared = mid * mid
            
        #     if mid_squared == x:
        #         return mid
        #     elif mid_squared < x:
        #         result = mid
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        
        # return result
        if x == 0:
            return 0
        first,last = 1, x
        result = 0
        while first <= last:
            mid = (first + (last)) //2     
            mid_squared = mid*mid  
            if mid_squared == x:
                return mid
            if mid_squared < x:
                result = mid
                first = mid+1
            if mid_squared >x:
                last = mid-1
        return result 
            