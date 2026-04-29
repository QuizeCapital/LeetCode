class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        a, b = 0, 1
        for val in range(2, n+1):
            a, b = b, a + b
            # print(a, b)
        return b 
        
        