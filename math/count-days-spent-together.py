class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        # leaveAlice_last_day = int(leaveAlice.split('-')[1])
        # leaveAlice_mon = int(leaveAlice.split('-')[0])
        # arriveBob_first_day = int(arriveBob.split('-')[1])
        # arriveBob_mon = int(arriveBob.split('-')[0])
        # if leaveAlice_mon >= arriveBob_mon:
        #     return abs(arriveBob_first_day - leaveAlice_last_day)+1
        # return 0
        def d(s):
            return date(2022, *map(int, s.split('-')))
        
        first = d(max(arriveAlice, arriveBob))
        last = d(min(leaveAlice, leaveBob))

        return max(0, (last - first).days + 1)
        