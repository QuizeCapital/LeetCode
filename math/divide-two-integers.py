class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = 0
        if (divisor > 0 and dividend > 0) or (divisor<0 and dividend<0): 
            positive = 1
        
        dividend, divisor = abs(dividend), abs(divisor)

        current_val, coef, answer = divisor, 1, 0

        while divisor <= dividend:
            if current_val + current_val <= dividend:
                current_val += current_val
                coef += coef
            else:
                answer += coef
                dividend -= current_val
                current_val, coef = divisor, 1
        if positive == 1 and answer == 2**31:
            return 2**31 - 1
        
        return answer if positive == 1 else -answer


        