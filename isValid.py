class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {
            '{':'}',
            '(':')',
            '[':']'
        }
        tmp = []
        for i in range(len(s)):
            if s[i] not in d:
                return False
            else:
                tmp.append(s[i])
            if s[i] == d.get(i):
                tmp.pop()
                