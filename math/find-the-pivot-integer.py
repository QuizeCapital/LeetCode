class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        list_n = range(n+1)
        len_n = len(list_n)
        for i in range(n+1):
            sum_first = sum(list_n[:i+1])
            sum_last = sum(list_n[i:])

            if sum_first == sum_last:
                return i

        return -1

        if sum_last == sum_first:
            return i



        # return range(1, n+1)