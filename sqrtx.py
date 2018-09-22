class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x
        while low <= high:
            mid = (low + high) / 2
            if mid * mid == x: return int(mid)
            elif mid * mid < x: low = int(mid + 1)
            else: high = int(mid - 1)
        return high
