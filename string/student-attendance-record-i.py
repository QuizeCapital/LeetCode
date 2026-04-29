class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Rule 1: fewer than 2 'A's
        if s.count('A') >= 2:
            return False

        # Rule 2: no "LLL" substring
        if 'LLL' in s:
            return False

        return True
    
print(Solution().checkRecord("AA"))