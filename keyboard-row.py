class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        count = None
        res = []
        l1 = {'q': 0, 'w': 0, 'e': 0, 'r': 0, 't': 0, 'y': 0, 'u': 0, 'i': 0, 'o': 0, 'p': 0}
        l2 = {'a': 0, 's': 0, 'd': 0, 'f': 0, 'g': 0, 'h': 0, 'j': 0, 'k': 0, 'l': 0}
        l3 = {'z': 0, 'x': 0, 'c': 0, 'v': 0, 'b': 0, 'n': 0, 'm': 0}
        words2 = list(map(lambda x: x.lower(), words))
        for i in range(len(words2)):
            if l1.get(words2[i][0], -1) != -1: count = 1
            elif l2.get(words2[i][0], -1) != -1: count = 2
            elif l3.get(words2[i][0], -1) != -1: count = 3
            for j in range(len(words2[i])):
                if count == 1 and l1.get(words2[i][j], -1) == -1: break
                if count == 2 and l2.get(words2[i][j], -1) == -1: break
                if count == 3 and l3.get(words2[i][j], -1) == -1: break
                if j == len(words2[i]) - 1: res.append(words[i])
        return res

