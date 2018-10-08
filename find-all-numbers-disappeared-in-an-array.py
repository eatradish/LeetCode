from collections import Counter
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        d = Counter(nums)
        for i in range(1, len(nums) + 1):
            if i not in d: res.append(i)
        return res
