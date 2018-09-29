class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l1 = list(s)
        l2 = list(t)
        l1.sort()
        l2.sort()
        while l1 != []:
            if l1[i] == l2[i]:
                tmp = l1[i]
                l1.remove(tmp)
                l2.remove(tmp)
            else: return l2[i]
        return l2[0]

s = Solution().findTheDifference("ae", "aae")
