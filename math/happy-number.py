class Solution(object):
    # def isHappy(self, n):
    #     """
    #     :type n: int
    #     :rtype: bool
    #     """
    #     if n>9:
    #         return False
    #     else:
    #         solution_set = set()
    #         while n != 1 :
    #             n = sum([int(i)**2 for i in str(n)])
    #             if n in solution_set:
    #                 return False 
    #             else:
    #                 solution_set.add(n)
    #     # else:
    #     #     return True
    
    def isHappy(self, n):
        mem = set()
        while n != 1 and n not in mem:
            mem.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        return n == 1

    # def isHappy(self, n):
    #     seen = set()
    #     while n != 1 and n not in seen:
    #         seen.add(n)
    #         n = sum(int(i) ** 2 for i in str(n))
    #     return n == 1
            

             
        
print(Solution().isHappy(2))
