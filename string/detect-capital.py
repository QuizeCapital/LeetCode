class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(list(word)) < 2:
            return True
        if word.isupper() or word.islower(): 
            return True
        if list(word)[0].isupper() and str(list(word)[1:]).islower():
            return True
        return False

