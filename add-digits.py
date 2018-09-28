class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        l = list(str(num))
        l = list(map(lambda x: int(x), l))
        num = sum(l)
        return num if len(str(num)) == 1 else self.addDigits(num)

