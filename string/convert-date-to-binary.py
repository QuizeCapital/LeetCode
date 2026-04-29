class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        parts = date.split('-')
        binary_parts = []
        for part in parts:
            number = int(part)
            binary_value = bin(number)[2:]
            binary_parts.append(binary_value)
        
        result = "-".join(binary_parts)
        return result