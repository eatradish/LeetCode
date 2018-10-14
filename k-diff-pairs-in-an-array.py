from collections import Counter
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        if k < 0: return 0
        if k == 0:
            count = 0
            c = Counter(nums)
            for i in c:
                if c[i] > 1: count += 1
            return count
        nums = set(nums)
        for i in nums:
            if i + k in nums: res += 1
        return res
