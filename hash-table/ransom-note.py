from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        st1, st2 = Counter(ransomNote), Counter(magazine)
        return st1 & st2 == st1