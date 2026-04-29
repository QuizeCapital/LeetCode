class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_ord = []
        t_ord = []
        # max_len = max(list(s), list(t))
        if len(s) != len(t):
            return False
        else:
            for idx in set(s):
                if s.count(idx) != t.count(idx):
                    return False 
            return True
print(Solution().isAnagram("ggii","eekk"))