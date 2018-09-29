class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = []
        no_see = []
        for i in s:
            if i not in l and i not in no_see: l.append(i)
            elif i in l:
                l.remove(i)
                no_see.append(i)
        return -1 if len(l) == 0 else s.index(l[0])
