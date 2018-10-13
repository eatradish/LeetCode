class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        nums1 = findNums
        nums2 = nums
        res = []
        for i in range(len(nums1)):
            index = nums2.index(nums1[i])
            for j in range(index + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    res.append(nums2[j])
                    break
                elif j == len(nums2) - 1: res.append(-1)
        return res
