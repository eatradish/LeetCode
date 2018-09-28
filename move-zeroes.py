class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        countZero = nums.count(0)
        while nums.count(0) != 0: nums.remove(0)
        for j in range(countZero): nums.append(0)
