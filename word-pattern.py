class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        d = {}
        l = str.split()
        if len(l) != len(pattern): return False
        for i in range(len(pattern)):
            if pattern[i] not in d and l[i] in d.values(): return False
            if pattern[i] not in d: d[pattern[i]] = l[i]
            if pattern[i] in d and l[i] != d[pattern[i]]: return False
        return True
