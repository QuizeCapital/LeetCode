class Solution(object):
    def getLeastFrequentDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        unique_nums = list(set(list(str(n))))
        unique_nums_dict = {i:int() for i in unique_nums}
        for i in (list(str(n))):
            if i in unique_nums_dict.keys():
                unique_nums_dict[i] += 1
        min_freq = min(unique_nums_dict.values())
        min_digits = [digit for digit, freq in unique_nums_dict.items() if freq == min_freq]

        return int(min(min_digits))