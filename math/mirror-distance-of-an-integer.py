class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        if len(str(n)) > 1:
            rev_n = str(n)[::-1]
            rev_n = int(''.join(rev_n))
        else:
            rev_n = n 

        mirror = abs(n - rev_n)

        return mirror