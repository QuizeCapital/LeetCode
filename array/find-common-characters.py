from collections import Counter
from functools import reduce
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return list(reduce(lambda a,b: a&b, map(Counter,words)).elements())

print(Solution().commonChars(["bella","label","roller"]))