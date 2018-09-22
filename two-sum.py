class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)): d[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d and d.get(complement) != i: return [i, d.get(complement)]
        return
s = Solution().twoSum([3,2,4],6)
print(s)
