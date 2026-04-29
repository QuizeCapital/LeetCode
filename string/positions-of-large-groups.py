class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        # final = []
        # dict_values = {i:[0,[]] for i in list(set(s))}
        # for ind, value in enumerate(s):
        #     print(value, s[ind-1])
        #     if value in dict_values and value == s[ind-1]:
        #         dict_values[value][0] += 1
        #         dict_values[value][1].append(ind)
        #     # else:
        #     #     break
        # for key,val in dict_values.items():
        #     if val[0] >=3:
        #         final.append([val[1][0], val[1][-1]])

        # return final

        final = []
        n = len(s)

        i = 0 
        while i < n:
            current_char = s[i]
            start = i

            count = 0 
            indices = []

            while i < n and s[i] == current_char:
                count += 1
                indices.append(i)
                i += 1
            
            if count >= 3:
                final.append([indices[0], indices[-1]])
        return final
        
    
print(Solution().largeGroupPositions("abcdddeeeeaabbbcd"))