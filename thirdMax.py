class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_max = nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        elif len(nums) == 1: return nums[0]
        else:
            nums = list(set(nums))
            for i in range(len(nums)):
                if nums[i] > nums_max: nums_max = nums[i]
            nums.remove(nums_max)
            if len(nums) != 0:
                nums_two_max = nums[0]
                for i in range(len(nums)):
                    if nums[i] > nums_two_max: nums_two_max = nums[i]
            else: return nums_max
            nums.remove(nums_two_max)
            if len(nums) != 0:
                nums_third_max = nums[0]
                for i in range(len(nums)):
                    if nums[i] > nums_third_max: nums_third_max = nums[i]
                return nums_third_max
            else: return nums_max

s = Solution().thirdMax([2,2,3,1])
print(s)