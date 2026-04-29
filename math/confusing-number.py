class Solution(object):
    def confusingNumber(self, n):
        """
        :type n: int
        :rtype: bool
        """
        map = {0:0, 1:1, 6:9, 8:8, 9:6}
        rotated, original = 0, n
        if n == 0:
            return False 

        while n > 0:
            digit = n % 10 

            if digit not in map:
                return False

            rotated = rotated * 10 + map[digit]

            n //= 10 

        return rotated != original 