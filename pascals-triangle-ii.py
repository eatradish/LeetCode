class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        l = [[1]]
        """
        l[0] = [1]
        l[1] = [l[0],l[0]]
        l[2] = [l[0], l[0] + l[1], l[1]]
        l[3] = [l[0], l[0] + l[1], l[1] + l[2], l[2]]
        l[4] = [l[0], l[0] + l[1], l[1] + l[2], l[2] + l[3], l[3]]
        """
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]
        for i in range(1, rowIndex+1):
            l2 = []
            if len(l) == 1:
                l2 = [l[0][0], l[0][-1]]
                l.append(l2)
                l2 = []
            else:
                l2.append(l[i-1][0])
                for j in range(len(l[i-1])-1): l2 = l2 + [l[i-1][j] + l[i-1][j+1]]
                l2.append(l[i-1][-1])
                l.append(l2)
                l2 = []
        return l[-1]
