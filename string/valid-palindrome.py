class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        removed_punct = [i.lower() for i in list(s) if i.isalnum() and i != '']
        print(removed_punct)
        print(removed_punct[::-1])
        if removed_punct == removed_punct[::-1]:
            return True
        return False


print(Solution().isPalindrome("OP"))