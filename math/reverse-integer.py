class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
        x = [i for i in list(str(x)) if i != '0' or i != '-']

        x = x[::-1]

        x = [str(i) for i in x]
        
        x = int("".join(x)) * sign
        if x < -2**31 or x > 2**31 - 1:
            return 0

        return x
        