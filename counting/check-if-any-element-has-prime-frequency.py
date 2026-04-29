class Solution(object):
    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        primes = set([
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
        53, 59, 61, 67, 71, 73, 79, 83, 89, 97
        ])
        nums_dict = {int(i):int() for i in nums}
        for i in nums: 
            if i in nums_dict.keys():
                nums_dict[i]+=1 
        # return bool(set(nums_dict.values()) & primes)
        return (set(nums_dict.values()) & primes) != set([])