class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack: return -1
        if needle == '': return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:len(needle)+i] == needle: return i
        return -1
