class Solution(object):
    def missingNumber(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr_sorted = sorted(arr)
        diff = arr_sorted[1] - arr_sorted[0] 
        # list_data = range(arr_sorted[0], arr_sorted[-1] + 1, diff)
        # missing_set = set(arr_sorted) ^ set(list_data)
        expected_total_sum = ((arr_sorted[0] + arr_sorted[-1]) * (len(arr_sorted) + 1) ) // 2
        actual_sum = sum(arr)
        return expected_total_sum - actual_sum
