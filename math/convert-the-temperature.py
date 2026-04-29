class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        temps = [
        ]
        kelv = celsius + 273.15
        fah = celsius * 1.8 +32
        return [kelv, fah]
        