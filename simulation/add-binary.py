class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        max_len = max(len(a), len(b))

        a = a.zfill(max_len)
        b = b.zfill(max_len)

        result = []
        carry = 0

        for i in range(max_len -1, -1, -1):
            bit_a = int(a[i])
            bit_b = int(b[i])

            total = bit_a + bit_b + carry 

            current_bit = total % 2 
            carry = total // 2

            result.append(str(current_bit))
        
        if carry:
            result.append('1')
        
        return "".join(result[::-1])