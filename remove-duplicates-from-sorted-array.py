class Solution:
    # ipython 与 LeetCode 输出结果不一样，但理论可行
    def removeDuplicates_a(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        return len(nums)

    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]: 
                i += 1
                nums[i] = nums[j]
        return i + 1

s = Solution().removeDuplicates([1,1,2])