class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        org_letters = letters
        letters = list(set(list(letters)+list(target)))
        target_ind_plus_one = sorted(letters).index(target) + 1

        if target != "z" and target_ind_plus_one < len(letters):
            return sorted(letters)[target_ind_plus_one]
        return org_letters[0]
