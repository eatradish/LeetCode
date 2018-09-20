class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        state_min = prices[0]
        state_max = 0
        for i in range(len(prices)):
            if prices[i] < state_min:
                state_min = prices[i]
            if prices[i] - state_min > state_max:
                state_max = prices[i] - state_min
        return state_max
            
