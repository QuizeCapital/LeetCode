class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        grid_values = range(1, (len(grid) * len(grid)) + 1)
        final = []
        results = []
        for val in grid:
            for value in val:
                if value not in final:
                    final.append(value)
                else:
                    results.append(value)
        results = results + (list(set(final) ^ set(grid_values))) 

        # return final, results, grid_values, (list(set(final) ^ set(grid_values))) 
        return results

        