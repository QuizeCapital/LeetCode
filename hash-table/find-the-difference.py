class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        s_sum = sum(ord(x) for x in s)
        t_sum = sum(ord(y) for y in t)
        return chr(t_sum-s_sum)

print(Solution().findTheDifference("abcd", "abcde"))
