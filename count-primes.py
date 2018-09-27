class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in [0, 1, 2]: return 0
        isPrime = [True] * (n)
        isPrime[0] = False
        isPrime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, n, i): isPrime[j] = False
        return isPrime.count(True)
