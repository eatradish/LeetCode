class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        l1 = list(ransomNote)
        l2 = list(magazine)
        i = 0
        while len(l1) != 0:
            if l1[i] not in l2: return False
            else:
                tmp = l1[i]
                l1.remove(tmp)
                l2.remove(tmp)
                i = 0
        return True

