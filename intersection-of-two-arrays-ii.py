class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        tmp = list(set(list(filter(lambda x: x in nums2, nums1))))
        res = []
        for i in range(len(tmp)):
            n = min(nums1.count(tmp[i]), nums2.count(tmp[i]))
            for j in range(n): res.append(tmp[i])
        return res
