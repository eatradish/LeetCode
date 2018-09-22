class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if i not in d: d[i] = 1
            else: del d[i]
        return [i for i in d][0]
