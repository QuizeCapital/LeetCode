class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        # # One complete cycle (back and forth)
        # cycle_length = 2 * (n - 1)
        
        # # Find where we are in the current cycle
        # time_in_cycle = time % cycle_length
        
        # if time_in_cycle < n:
        #     # Moving forward: 1 -> 2 -> ... -> n
        #     return time_in_cycle + 1
        # else:
        #     # Moving backward: n -> n-1 -> ... -> 1
        #     return 2 * n - time_in_cycle - 1
        cycle_len = 2 * (n - 1)
        time_in_cycle = time % cycle_len
        if time_in_cycle < n:
            return time_in_cycle + 1
        else :
            return (2 * n) - time_in_cycle - 1
        