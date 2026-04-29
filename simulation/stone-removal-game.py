class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        turn = False
        p = 10
        while n >= p:
            n -= p
            p -= 1
            turn = not turn 
        return turn