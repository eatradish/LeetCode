class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ''
        for i in range(len(digits)): s += str(digits[i])
        num = int(s)
        num = num + 1
        l = list(str(num))
        for i in range(len(l)): l[i] = int(l[i])
        return l