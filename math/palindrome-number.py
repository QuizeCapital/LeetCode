class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # return list(str(x))[::-1] == list(str(x))
        original = x
        reversed_num = 0
        while x > 0:
            last_digit = x % 10
            reversed_num = reversed_num * 10 + last_digit
            x = x//10 
        return original == reversed_num
        