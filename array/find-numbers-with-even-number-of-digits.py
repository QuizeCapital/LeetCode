class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # def findNumbers(self, nums):
        count = 0
        for i in nums:
            if self.count_digits(i) % 2 == 0:
                count += 1
        return count


    def count_digits(self, x):
        count = 0
        while  x > 0:
            x = x // 10
            count += 1
        return count