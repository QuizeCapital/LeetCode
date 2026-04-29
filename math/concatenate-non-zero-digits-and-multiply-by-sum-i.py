class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum_n = sum(int(x) for x in str(n))
        vals = ''.join([x for x in str(n) if x != '0'])
        if not vals:
            return 0

        return int(vals) * sum_n