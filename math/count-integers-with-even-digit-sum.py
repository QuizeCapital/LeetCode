class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        for i in range(1, num+1):
            digit_sum = 0
            n = i

            while n>0:
                digit_sum += n % 10
                n //= 10
            if digit_sum % 2 == 0:
                count += 1
        return count

 