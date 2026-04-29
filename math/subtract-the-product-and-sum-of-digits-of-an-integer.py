class Solution(object):
    import math
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        summed = sum(int(i) for i in list(str(n)))
        #multd = math.prod(int(i) for i in list(str(n))) 
        multd = 1
        for i in list(str(n)):
            multd *= int(i)

        return multd - summed
        