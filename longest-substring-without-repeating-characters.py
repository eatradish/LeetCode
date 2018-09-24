class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = []
        res = 0
        i = 0
        n = 0
        while n < len(s) and i < len(s):
            symbol = s[i:i + n]
            symbol2 = s[i + 1 + n:i + n + 2]
            if symbol == symbol2 and res < len(symbol): 
                res = len(symbol)
                n += 1
            else: i += 1

s = Solution().lengthOfLongestSubstring("au")