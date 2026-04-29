class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        dist1 = abs(x - z)  # distance of Person 1 from Person 3
        dist2 = abs(y - z) 
        if dist1 < dist2:
            return 1     # Person 1 reaches first
        elif dist2 < dist1:
            return 2     # Person 2 reaches first
        else:
            return 0 
        