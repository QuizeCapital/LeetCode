class Solution(object):
    def fixedPoint(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # for ind, val in enumerate(arr):
        #     if val == ind:
        #         return ind 
        # return -1

        start, end = 0, len(arr)-1 
        result = -1 

        while start <= end:
            mid = (start+end) //2
            if arr[mid] >= mid:
                if arr[mid] == mid:
                    result = mid 
                end = mid - 1
            else:
                start = mid + 1
        return result

