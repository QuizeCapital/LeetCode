class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = sorted(str(num))
        num1 = []
        num2 = []
        for i, digs in enumerate(digits):
            if i % 2 == 0:
                num1.append(digs)
            else:
                num2.append(digs)

        return int(''.join(num1)) + int(''.join(num2))
        