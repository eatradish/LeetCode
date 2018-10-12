class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                if len(nums[:i]) > res: res = len(nums[:i])
                nums = nums[i + 1:]
                i = 0
            else: i += 1
        if len(set(nums)) == 1 and nums[0] == 1 and res < len(nums): res = len(nums)
        return res
