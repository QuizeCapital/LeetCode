class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        ways = 0

        for a in range( limit + 1):
            remaining = n - a

            max_b = min(remaining, limit)
            #c  = n -(max_b + remaining )
            c = max(0, remaining - limit) 

            if c <= max_b:
                ways += ((max_b - c) + 1)

        return ways 
        