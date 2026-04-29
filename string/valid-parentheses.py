class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for sign in s:
            if sign in pairs.values():
                stack.append(sign)
            elif sign in pairs.keys():
                if not stack or stack[-1] != pairs[sign]:
                    return False 
                stack.pop()
            else:
                return False 
            
        return not stack