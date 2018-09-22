import string
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        res = 0
        str26 = string.ascii_uppercase
        for i in range(len(str26)): d[str26[i]] = i + 1
        if s in d: return d[s]
        for i in range(len(s)): res = res * 26 + d[s[i]]
        return res
