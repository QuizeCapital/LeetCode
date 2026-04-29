class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        n = len(coordinates)
        if n <= 2:
            return True 

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        if x2 - x1 == 0:
            for i in range(2, n):
                if coordinates[i][0] != x1:
                    return False 
            return True 

        slope = (y2 -y1) / (x2 -x1)

        for i in range(2, n):
            x, y = coordinates[i]
            if x - x1 == 0:
                return False
            current_slope = (y - y1) / (x - x1)
            # if current_slope != slope:
            if (y2 - y1) * (x - x1) != (y - y1) * (x2 - x1):
                return False 

        return True 
        # while n > 0:
        #     for num in range(len(coordinates)): 
        #         if coordinates[num + 1][0] - coordinates[num][0] == 1 and coordinates[num + 1][1] - coordinates[num][1] == 1:
        #             return True 
        #         n =- 1
        # return False
