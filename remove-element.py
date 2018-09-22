class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(val)
                i = 0
            else: i += 1
        return len(nums)
s = Solution().removeElement([3,2,2,3], 2)