import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = s
        a = a.lower()
        r = re.sub(r'[^a-zA-Z0-9_]',"", a)
        return r == r[::-1]

