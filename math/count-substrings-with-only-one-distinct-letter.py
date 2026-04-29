class Solution(object):
    def countLetters(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 1
        n = len(s) - 1
        counter = 1

        for i in range(n):
                if s[i] == s[i+1]:
                    counter += 1
                else:
                    counter = 1
                res += counter
        return res
        