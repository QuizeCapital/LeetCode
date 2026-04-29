class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l = []
        pairs = n // 2
        for i in range(1, pairs + 1):
            l.append(i)
            l.append(-i)
        
        if n % 2 == 1:
            l.append(0)
        
        return l
        