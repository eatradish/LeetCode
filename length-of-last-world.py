class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or list(set(s)) == [' ']:
            return 0
        else:
            return len((s.split())[-1])