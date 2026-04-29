class Solution(object):
    def smallestNumber(self, n, t):
        current_number = n
        while True:
            temp = current_number 
            product = 1

            while temp > 0:
                last_digit = temp % 10 # Get the last digit
                product *= last_digit 
                temp = temp // 10 # Remove the last             
            if product % t == 0:
                return current_number       
            current_number += 1