class Solution(object):
    def isArmstrong(self, n):
        """
        :type n: int
        :rtype: bool
        """
        list_n = list(str(n))
        len_n = len(list_n)

        sum_n = sum(int(i)**len_n for i in list_n)
        return sum_n == n