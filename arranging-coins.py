class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 1
        while n >= k:
            n = n - k
            k += 1
        return k - 1
