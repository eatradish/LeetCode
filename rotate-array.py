class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < k:
            nums.insert(0, nums[-1])
            nums.pop()
            i += 1
