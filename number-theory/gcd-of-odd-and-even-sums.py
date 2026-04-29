class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum_odd = n * n 
        sum_even = n * (n + 1)

        a, b = sum_odd, sum_even 
        while b:
            a, b = b, a % b

        return a
        