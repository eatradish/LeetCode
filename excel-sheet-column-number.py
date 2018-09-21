import string
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        res = 0
        for i in range(len(string.ascii_uppercase)):d[string.ascii_uppercase[i]] = i + 1
        if s in d:return d[s]
        for i in range(len(s)):res = res * 26 + d[s[i]]
        return res
