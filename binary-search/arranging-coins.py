class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        row_count = 0
        row = 0

        while n >= row_count:
            # for i in range(n):
            row = row+1
            row_count += n-(n-row)
        return row -1

print(Solution().arrangeCoins(8))