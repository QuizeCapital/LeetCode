class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        count = 0
        max_val = max(a, b)
        min_val = min(a, b)
        for i in range(1, min_val + 1):
            if min_val % i == 0 and max_val % i == 0 :
                count += 1
        return count 
# class Solution(object):
#     def commonFactors(self, a, b):
#         count = 0
#         for i in range(1, min(a, b) + 1):
#             if a % i == 0 and b % i == 0:
#                 count += 1
#         return count