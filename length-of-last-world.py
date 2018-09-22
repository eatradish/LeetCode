class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return 0 if len(s) == 0 or list(set(s)) == [' '] else len((s.split())[-1])