class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d: d[nums[i]] = 1
            else: d[nums[i]] += 1
        return sorted(d.items(), key = lambda d:d[1], reverse = True)[0][0]
