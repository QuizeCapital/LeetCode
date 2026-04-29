class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        values = [i for i in range(1, 27)]
        letter_to_number = dict(zip(letters, values))

        result = 0 

        for ch in columnTitle: 
            result = result *26 + letter_to_number[ch]

        return result 