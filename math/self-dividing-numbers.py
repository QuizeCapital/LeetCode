class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []

        def divider(m):
            ok = True
            while m:
                d = m % 10
                if d == 0 or n % d != 0:
                    return False
                m //= 10
            return True
        for n in range(left, right + 1):
            if divider(n):
                res.append(n)
        return res