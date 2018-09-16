class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = numbers
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i+1
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d and d.get(complement) != i+1:
                return [i+1, d.get(complement)]