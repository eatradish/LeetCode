from copy import copy
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        d = {}
        for i in s:
            if i not in d: d[i] = 1
            else: d[i] += 1
        l = list(d.values())
        a = copy(l)
        i = 0
        while i < len(a):
            if a[i] % 2 == 0:
                a.remove(a[i])
                i = 0
            else: i += 1
        if a == []: max_num = 0
        else: max_num = max(a)
        for i in l:
            if i % 2 == 0: res += i
            elif i % 2 != 0 and i != max_num: res += i - 1
        if l.count(max_num) > 1: res += max_num + (max_num - 1) * (l.count(max_num) - 1)
        else: res += max_num
        return res
