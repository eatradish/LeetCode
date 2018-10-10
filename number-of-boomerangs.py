class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for pa in points:
            d = {}
            for pb in points:
                length = (pa[0] - pb[0]) ** 2 + (pa[1] - pb[1]) ** 2
                d[length] = d.get(length, 0) + 1
            res += sum(i * (i - 1) for i in d.values())
        return res
