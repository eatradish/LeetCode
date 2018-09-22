import string

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        d = {}
        l = []
        res = ''
        a = ''
        s = string.ascii_uppercase
        for i in range(len(s)): d[i + 1] = s[i]
        if n in d: return d[n]
        if n % 26 == 0:
            n = n / 26 - 1
            a ='Z'
        while n > 26:
            b = n % 26
            n = n // 26
            l.append(b)
        res = d[n]
        for i in l[::-1]: res += d[i]
        res += a
        return res

