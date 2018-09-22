class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        l = []
        index = 0
        while index < len(s):
            symbol = s[index]
            if symbol in d.values(): l.append(symbol)
            else:
                if l == []: return False
                if symbol in d and l[-1] != d[symbol]: return False
                l.pop()
            index += 1
        return l == []