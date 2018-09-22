class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for j in range(len(A[0])):
            l = []
            for i in range(len(A)): l.append(A[i][j])
            result.append(l)
        return result