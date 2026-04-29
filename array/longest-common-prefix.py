class Solution(object):
    # def longestCommonPrefix(self, strs):
        # """
        # :type strs: List[str]
        # :rtype: str
        # """
        # min_value = min(strs, key = len)
        # # print(min_value)
        # for i in strs:
        #     while not i.startswith(min_value):
        #         min_value = min_value[:-1]

        # return min_value
        # for enum, i in enumaerate()

    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        min_value = min(strs, key=len)
        final_str = ''
        
        for enum, char in enumerate(min_value):
            for word in strs:
                if word[enum] != char:
                    return final_str
            final_str += char
        
        return final_str


print(Solution().longestCommonPrefix(["flower","flow","flight"]))