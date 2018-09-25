class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        no_happy_nums = [4, 16, 37, 58, 89, 145, 42, 20]
        while n != 1:
            s = str(n)
            l = list(map(lambda x: int(x), s))
            n = sum(list(map(lambda x: x ** 2, l)))
            if n in no_happy_nums: return False
        return True
