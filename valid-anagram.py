class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ds = {}
        dt = {}
        if len(s) != len(t): return False
        for i in s:
            if i not in ds: ds[i] = 1
            else: ds[i] += 1
        for i in t:
            if i not in dt: dt[i] = 1
            else: dt[i] += 1
        if ds != dt: return False
        return True

