class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        sign_ = 1

        for i in str(n):
            total += sign_ * int(i)
            sign_ *= -1

        return total
        