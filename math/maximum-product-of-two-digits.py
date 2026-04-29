class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        list_n = list(str(n))
        sorted_num = sorted(list_n)
        res = 1
        for i in sorted_num[-2:]:
            res *= int(i)


        return res
        