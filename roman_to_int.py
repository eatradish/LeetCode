class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {
                'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000
                }
        result = 0
        if s in d:
            result += d[s]
        else:
            for i in range(len(s)):
                if s[i] not in d:
                    return
                else:
                    result += d[s[i]]
                    if i == len(s) - 1:
                        break
                    if d[s[i+1]] > d[s[i]]: 
                        result -= 2 * d[s[i]]
            return result
                

s = Solution().romanToInt('III')
print(s)
