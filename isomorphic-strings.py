class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.test(s, t) and self.test(t, s)
    def test(self, s, t):
        d = {}
        for i in range(len(s)):
            if s[i] not in d: d[s[i]] = t[i]
            elif d[s[i]] != t[i]: return False
        return True
