class Solution(object):
    def numberOfDays(self, year, month):
        """
        :type year: int
        :type month: int
        :rtype: int
        """
        if month in [1, 3, 5,7,8,10,12]:
            return 31
        elif month != 2: 
            return 30 
        else:
            return 28 + (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
        