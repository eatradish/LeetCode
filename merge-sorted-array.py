class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        while j < len(nums2):
            for i in range(len(nums1)):
                if nums1[i] == 0 and i >= m:
                    nums1[i] = nums2[j]
                    j += 1
        nums1.sort()