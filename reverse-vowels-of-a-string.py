class Solution:
    # 参考自 https://blog.csdn.net/qq_17550379/article/details/80515302
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'u', 'e', 'i', 'o', 'A', 'U', 'E', 'I', 'O']
        p = [i for i in s if i in vowels]
        return ''.join([i if i not in vowels else p.pop() for i in s])
