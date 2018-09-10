class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        tmp = []

        if '' in strs or len(strs) == 0:
            return result

        min_len = len(strs[0])

        for i in range(len(strs)):
            if len(strs[i]) < min_len:
                min_len = len(strs[i])

        for j in range(1, min_len+1):
            for i in range(len(strs)):
                tmp.append(strs[i][:j])
            if len(set(tmp)) == 1:
                tmp = []
                result = strs[i][:j]
        return result
            

                
        


s = Solution().longestCommonPrefix([])
print(s)
# strs[0][0] strs[1][0]
# strs[0][1] strs[1][1]

# strs[0][0] strs[1][0] strs[2][0] .... strs[n][0]
# strs[0][1] ....strs[n][1]
# flow 
# flow -> flo



### remove item
# oooo oook oooe -> ooo