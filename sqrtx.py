    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1: return 1
        low = 0
        high = x
        while low <= high:
            mid = low + (high - low) // 2
            if mid == x / mid: return mid
            elif mid < x / mid: low = mid + 1
            else: high = mid - 1
        return high
