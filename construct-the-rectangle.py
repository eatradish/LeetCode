from math import sqrt
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        area_sqrt = int(sqrt(area))
        l = area
        w = 1
        for i in range(area_sqrt, 0, -1):
            if area % i == 0:
                l = area // i
                w = i
                break
        return [l, w]

