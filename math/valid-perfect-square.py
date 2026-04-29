class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        root_num = num ** 0.5
        values = 0
        while values <=  root_num:
            if values * values ==  num:

                return True
            values += 1
                # print(values)
        return False
       
    
# print(Solution().isPerfectSquare(14))