class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Convert the number to a list of digits (as strings)
        digits = list(str(num))
        
        # Record the last position of each digit (0-9)
        last_position = {}
        for i, d in enumerate(digits):
            last_position[int(d)] = i

        # Go through each digit from left to right
        for i in range(len(digits)):
            current_digit = int(digits[i])

            # Look for a larger digit that appears later
            # We'll check from 9 down to current_digit + 1
            larger_digit = 9
            while larger_digit > current_digit:
                # If we find a larger digit that occurs later
                if larger_digit in last_position and last_position[larger_digit] > i:
                    # Swap the current digit with that larger one
                    swap_index = last_position[larger_digit]
                    digits[i], digits[swap_index] = digits[swap_index], digits[i]

                    # Return the new number immediately (only one swap allowed)
                    return int(''.join(digits))
                larger_digit -= 1  # check the next smaller digit
        
        # If no better swap found, return the original number
        return num