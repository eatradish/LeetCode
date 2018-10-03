class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res_l = []
        l1 = list(num1)
        l2 = list(num2)
        count = 0
        res = ''
        if len(l1) > len(l2):
            for i in range(len(l1) - len(l2)): l2.insert(0, '0')
        elif len(l1) < len(l2):
            for i in range(len(l2) - len(l1)): l1.insert(0, '0')
        for i in range(len(l1) - 1, -1, -1):
            if int(l1[i]) + int(l2[i]) + count >= 10 and i != 0:
                a = str(int(l1[i]) + int(l2[i]) - 10 + count)
                count = 1
                res_l.append(a)
            else:
                a = str(int(l1[i]) + int(l2[i]) + count)
                count = 0
                res_l.append(a)
        for i in res_l[::-1]: res = res + i
        return res
