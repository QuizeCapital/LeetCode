class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_roman = {'I' :1, 
                    'V' : 5,
                    'X': 10,
                    'L':50,
                    'C':100,
                    'D':500,
                    'M': 1000
                    }
        val = 0
        for i in range(len(s)-1):
            if dict_roman[s[i]] < dict_roman[s[i+1]]:
                val = val - dict_roman[s[i]]
            else:
                val = val + dict_roman[s[i]]
        return val + dict_roman[s[-1]]

            
