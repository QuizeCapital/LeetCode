class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        rounded_amount = ((purchaseAmount + 5) // 10) * 10
        return 100 - rounded_amount