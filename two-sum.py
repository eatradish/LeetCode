class Solution:
    # 时间超出限制
    def twoSum_a(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if i == len(nums) - 1:
                break
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
    
    # 字典法
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d and d.get(complement) != i:
                return [i, d.get(complement)]

s = Solution().twoSum([3,2,4],6)
print(s)
