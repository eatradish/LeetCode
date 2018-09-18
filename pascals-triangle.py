class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l = [[1]]
        """
        l[0] = [1]
        l[1] = [l[0],l[0]]
        l[2] = [l[0], l[0] + l[1], l[1]]
        l[3] = [l[0], l[0] + l[1], l[1] + l[2], l[2]]
        l[4] = [l[0], l[0] + l[1], l[1] + l[2], l[2] + l[3], l[3]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return l
        for i in range(1, numRows):
            l2 = []
            if len(l) == 1:
                l2 = [l[0][0], l[0][-1]]
                l.append(l2)
                l2 = []
            else:
                l2.append(l[i-1][0])
                for j in range(len(l[i-1])-1):
                    l2 = l2 + [l[i-1][j] + l[i-1][j+1]]
                l2.append(l[i-1][-1])
                l.append(l2)
                l2 = []
        return l
