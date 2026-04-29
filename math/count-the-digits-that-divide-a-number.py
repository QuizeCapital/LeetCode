class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # count = 0
        # for i in list(str(num)):
        #     if num % int(i) == 0:
        #         count += 1
        # return count

        count = 0 
        temp = num 

        while temp > 0:
            last_digit = temp % 10

            if last_digit != 0 and num % last_digit == 0:
                count+=1
            temp = temp // 10 


        return count
        