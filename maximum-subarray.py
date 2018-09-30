class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        sp = nums[0]
        for i in nums[1:]:
            if sp > 0: sp += i
            else: sp = i
            res = sp if sp > res else res
        return res
