from functools import reduce
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if len(deck) == 1:
            return False 
        
        res = {}

        for i in deck:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        
        vals = list(res.values())
        g = reduce(gcd, vals)

        # check if gcd >= 2
        return g >= 2

print(Solution().hasGroupsSizeX([1,1,1,2,2,2,3,3]))