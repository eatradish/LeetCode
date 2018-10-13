class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums_sort = sorted(nums, reverse = True)
        d = {}
        for i in nums: d[i] = 0
        for i in range(len(nums_sort)):
            if i == 0: d[nums_sort[i]] = "Gold Medal"
            elif i == 1: d[nums_sort[i]] = "Silver Medal"
            elif i == 2: d[nums_sort[i]] = "Bronze Medal"
            else: d[nums_sort[i]] = str(i + 1)
        for i in range(len(nums)): nums[i] = d[nums[i]]
        return nums


