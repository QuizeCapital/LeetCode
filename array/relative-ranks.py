class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        awards = {
            1 : 'Gold Medal'
            ,2 : 'Silver Medal'
            ,3 : 'Bronze Medal'
        }
        score_sort = sorted(score, reverse = True)
        # score_sort.sort(reverse=True)
        final = [""] * len(score)
        for rank, value_rank in enumerate(score_sort, start=1):
            for pos, value_score in enumerate(score):
                if value_rank == value_score: #and rank == 1 or value_rank == value_score and rank == 2 or value_rank == value_score and rank == 3:
                    if rank in awards:    
                        final[pos] = awards[rank]
                    else:
                        final[pos] = str(rank)
        return final

# print(Solution().findRelativeRanks([2,3,0,9,4]))