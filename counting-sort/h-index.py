class Solution(object):
    # def hIndex(self, citations):
    #     """
    #     :type citations: List[int]
    #     :rtype: int
    #     """
    #     if len(citations) == 1: 
    #         return citations[0]
    #     n = len(citations)
    #     citations.sort()

    #     left,right = 0, n 

    #     while left < right:
    #         mid = (left + right ) // 2
    #         new_left = n - mid
    #         if citations[new_left] >= mid:
    #             left = mid - 1
    #         else:
    #             right = mid + 1

    #     return left 
    # from typing import List

    def hIndex(self, citations):
        citations.sort()        # ascending
        n = len(citations)

        lo, hi = 0, n - 1
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            papers_with_at_least_mid = n - mid   # number of papers from mid..n-1
            if citations[mid] >= papers_with_at_least_mid:
                ans = papers_with_at_least_mid   # this h works; try to improve by moving left
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
