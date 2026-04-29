class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum_res = num
        while len(list(str(sum_res))) != 1:
            new_sum = sum(int(digit) for digit in str(sum_res))
            sum_res = new_sum
        return sum_res

# print(Solution().addDigits(54))