class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year_list = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334] 
        day = int(date[-2:])
        year = int(date[:4])
        month = int(date[5:7])

        if year % 4 == 0 and year != 1900 and month > 2:
            day += 1

        return year_list[month - 1] + day

        